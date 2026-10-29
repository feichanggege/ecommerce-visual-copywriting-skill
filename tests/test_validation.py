"""Regression checks for the verifier, saved-output evaluator and upload package."""
import copy
import importlib.util
import json
import runpy
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]


def load(filename):
    spec = importlib.util.spec_from_file_location(filename.replace("-", "_"), ROOT / "tools" / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


verifier = load("verify-skill.py")
evaluator = load("evaluate-prompts.py")
packager = load("package-skill.py")
count_copy = runpy.run_path(str(ROOT / "scripts/count-copy.py"))["count"]


class ValidationRegression(unittest.TestCase):
    def setUp(self):
        self.case = {
            "name": "food", "prompt": "普通食品详情页", "expected_behavior": ["排除功效"],
            "must_include": [["证据账本", "evidence ledger"]],
            "must_not_include": ["乌发", "FDA approved"], "final_copy_required": True,
        }

    def test_copy_counts_use_final_strings_including_punctuation(self):
        self.assertEqual(count_copy("小厨房，按需伸缩", "zh"), 8)
        self.assertEqual(count_copy("按需伸缩，适配台面", "zh"), 9)
        self.assertEqual(count_copy("小厨房也能灵活收纳", "zh"), 9)
        self.assertEqual(count_copy("39元\t 2只", "zh"), 5)
        self.assertEqual(count_copy("See the mechanism before choosing a size", "en"), 7)

    def test_real_lowercase_english_ledger_is_accepted(self):
        english = (ROOT / "SKILL.en.md").read_text(encoding="utf-8").replace("Evidence ledger", "evidence ledger")
        verifier.require_text("SKILL.en.md", english, ["Evidence ledger"])
        with self.assertRaisesRegex(ValueError, "missing expected text"):
            verifier.require_text("SKILL.en.md", "unrelated content", ["Evidence ledger"])

    def test_missing_english_failure_section_is_rejected(self):
        chinese = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        english = (ROOT / "SKILL.en.md").read_text(encoding="utf-8")
        verifier.check_bilingual_sections(chinese, english)
        with self.assertRaisesRegex(ValueError, "bilingual contract"):
            verifier.check_bilingual_sections(chinese, english.replace("## Key failure modes", "### Key failure modes"))

    def test_analysis_may_quote_risky_phrase_but_final_copy_may_not(self):
        response = {"name": "food", "response": "Evidence ledger: 不使用乌发。最终稿：黑芝麻食品", "final_copy": "黑芝麻食品"}
        self.assertEqual(evaluator.evaluate([self.case], [response]), [])
        response["final_copy"] = "乌发"
        failures = evaluator.evaluate([self.case], [response])
        self.assertTrue(any("forbidden final-copy phrase" in item for item in failures))

    def test_missing_markers_empty_final_and_selective_rewrite_are_rejected(self):
        response = {"name": "food", "response": "普通食品", "final_copy": ""}
        failures = evaluator.evaluate([self.case], [response])
        self.assertTrue(any("final_copy is required" in item for item in failures))
        self.assertTrue(any("missing required marker" in item for item in failures))
        response.update(response="证据账本：乌发", final_copy="黑芝麻食品")
        self.assertTrue(any("exact excerpt" in item for item in evaluator.evaluate([self.case], [response])))

    def test_markers_ignore_case_but_final_copy_preserves_exact_source(self):
        response = {"name": "food", "response": "EVIDENCE LEDGER. Final copy: SKU ABC", "final_copy": "SKU ABC"}
        self.assertEqual(evaluator.evaluate([self.case], [response]), [])
        response["final_copy"] = "sku abc"
        self.assertTrue(any("exact excerpt" in item for item in evaluator.evaluate([self.case], [response])))

    def test_required_visible_conditions_cannot_exist_only_in_analysis(self):
        case = dict(self.case, must_include_final=[["测试条件", "test conditions"], "低档"])
        response = {"name": "food", "response": "证据账本：测试条件为低档。最终稿：风扇", "final_copy": "风扇"}
        self.assertEqual(sum("required final-copy marker" in item for item in evaluator.evaluate([case], [response])), 2)
        response.update(response="证据账本。最终稿：风扇；TEST CONDITIONS：低档", final_copy="风扇；TEST CONDITIONS：低档")
        self.assertEqual(evaluator.evaluate([case], [response]), [])
        with self.assertRaisesRegex(ValueError, "must_include_final"):
            evaluator.validate_cases([dict(case, must_include_final=[])])

    def test_duplicate_unknown_missing_and_invalid_case_are_rejected(self):
        response = {"name": "food", "response": "证据账本：黑芝麻食品", "final_copy": "黑芝麻食品"}
        with self.assertRaisesRegex(ValueError, "duplicate response"):
            evaluator.evaluate([self.case], [response, response])
        with self.assertRaisesRegex(ValueError, "unknown response"):
            evaluator.evaluate([self.case], [dict(response, name="unknown")])
        self.assertTrue(any("missing response" in item for item in evaluator.evaluate([self.case], [])))
        broken = copy.deepcopy(self.case)
        broken["must_not_include"] = [["乌发"]]
        with self.assertRaisesRegex(ValueError, "invalid must_not_include"):
            evaluator.validate_cases([broken])

    def test_local_file_links_are_checked_relative_to_document(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            doc = root / "README.md"
            (root / "a b.md").write_text("ok", encoding="utf-8")
            verifier.check_local_links(root, doc, "[valid](a%20b.md) [web](https://example.com)")
            verifier.check_local_links(root, doc, '[valid](a%20b.md "A title") [angle](<a b.md> "A title")')
            with self.assertRaisesRegex(ValueError, "broken local file link"):
                verifier.check_local_links(root, doc, '<img src="missing.jpg">')
            with self.assertRaisesRegex(ValueError, "broken local file link"):
                verifier.check_local_links(root, doc, "[escape](../outside.md)")

    def test_upload_zip_has_one_skill_root_and_all_runtime_references(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / "skill.zip"
            packager.package(output)
            with ZipFile(output) as archive:
                self.assertIsNone(archive.testzip())
                names = archive.namelist()
                prefix = "ecommerce-visual-copywriting/"
                self.assertTrue(all(name.startswith(prefix) for name in names))
                for file in ["SKILL.md", "SKILL.en.md", "references/output-contracts.md",
                             "references/source-notes.md", "examples/durian-worked-example.md", "scripts/count-copy.py"]:
                    self.assertIn(prefix + file, names)
                self.assertFalse(any("/.git/" in name or "/assets/" in name or "/tests/" in name or "/docs/" in name for name in names))
            with self.assertRaisesRegex(ValueError, "overwrite a runtime resource"):
                packager.package(ROOT / "SKILL.md")

    def test_repository_checks_and_all_prompt_schemas(self):
        cases = json.loads((ROOT / "test-prompts.json").read_text(encoding="utf-8"))
        self.assertEqual(len(evaluator.validate_cases(cases)), 20)
        verifier.verify()


if __name__ == "__main__":
    unittest.main()
