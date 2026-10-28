# Contributing

Help improve a practical skill for evidence-based e-commerce visual plans, on-image copy, designer handoff, and localization.

## Report a problem

Use the issue templates for bugs, rule/source updates, or example requests. Include the runtime/model if known, category/market/platform, redacted inputs, actual output, expected behavior, and the location of the problem. Remove private customer information, credentials and non-public business data.

For rule suggestions, include an official URL, title, relevant provision, applicable market/category, effective date if available, and access date. Distinguish a legal requirement, platform policy, conservative practice, and style preference. A policy-center landing page does not prove a specific restriction.

## Make a focused change

- Read `SKILL.md`, the relevant reference, and `references/output-contracts.md` when changing output.
- Preserve the v3 workflow: evidence ledger, six drivers, Campaign Style Lock, Storyboard, execution cards, hard blockers and five Pass/Fail gates.
- Keep Chinese and English decision rules and sections aligned, including failure modes.
- Preserve explicit user mode choices. Missing evidence must not be invented; default model prompts reserve whitespace for later typography.
- Update applicable source notes, examples, prompt expectations and the Unreleased changelog.
- Keep each raster showcase asset at or below 500,000 bytes. Preserve product identity and complete image framing; link every public asset from documentation.
- Do not add new dependencies when the standard library suffices.

## Validate

```text
python tools/verify-skill.py
python -m unittest discover -s tests -v
python tools/package-skill.py --output dist/ecommerce-visual-copywriting.zip
```

If Claude Code is installed, also run `claude plugin validate .` after plugin metadata changes.

For behavior changes, run representative requests with the revised skill. Save the full response plus a separate `final_copy` field containing only publishable copy, then evaluate:

```text
python tools/evaluate-prompts.py --responses path/to/responses.json
```

The response format and matching rules are in [examples/README.md](examples/README.md). An evaluator Pass means specified text expectations passed; it does not prove legal compliance, visual quality, or all model behavior. Review claims, source scope, text rendering, mobile legibility, and product fidelity manually where relevant.

GitHub Actions runs static verification, evaluator regression tests, and packaging. Remote CI is confirmed only by the run result after a push/PR.

## Review and release

Use the PR template to explain the trigger, resulting behavior, sources, validation and any pending acceptance. Substantive rules require human maintainer review. Keep unreleased changes under Unreleased in [CHANGELOG.md](CHANGELOG.md). Existing release tags are immutable project history; publish a new version only after review, and keep marketplace/plugin versions aligned.

This project does not provide legal advice or guarantee platform approval. Contributions are released under the repository's MIT License.
