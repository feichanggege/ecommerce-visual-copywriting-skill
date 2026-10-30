# Changelog

## Unreleased

### Changed

- Stop instructing the model to keep placeholders for unproven claims: Needs-proof items are rewritten neutrally or deleted and listed in a pending-confirmation list outside the copy.
- Evidence ledger gains source types (documentary proof, supplier claim, visual observation, guesswork); only proof and cross-checked supplier claims enter finished copy, and specification areas hold Verified data only.
- Add listing/first-screen/cover rules, a five-step decision order, a three-part check for FAQ questions and an explicit list of content the image model must not generate; drop the annotation column from the kickoff questionnaire table.
- Make KV1 identify the product before secondary features: use a clear confirmed original name in the headline, retain original-to-short-name mappings where needed, and check recognition without support copy. Preserve no-added-text placements and allow later images to lead with features.
- Synchronize Chinese/English guidance, output contracts, platform playbooks and README examples; keep the universal naming rule in the runtime and retain only as examples the confirmed names “飘带裙摆项链” and “飘带流苏长项链” without inferred renaming or material/bundle claims.
- Restore the 80-point self-review as an anchored gate: five dimensions scored 0–100 against required conditions, any dimension below 80 rewritten (max two rounds) before delivery, and a self-review record attached to every delivery. Missing record or an under-80 final draft is a hard blocker. Self-review is stated as the first core principle and is not a pause in one-shot mode.
- Replace the Chinese and English README workflow diagrams with step/action/output tables. Align the summaries and deliverable lists with the current routing, evidence, text-rendering and acceptance rules.

### Fixed

- Make release text checks case-insensitive; cover bilingual section drift, broken local links, oversized/unreferenced showcase assets, prompt schemas and packaging.
- Replace the obsolete v1 overview and archive its internal polishing report.
- Compress showcase files and restore the complete durian thumbnail framing.
- Prevent unsupported performance inferences from product structure and require copy counts to match final strings.

### Added

- Seven behavioral scenarios for the two original necklace names, no-added-text KV1, later feature images non-jewelry recognition, missing-name kickoff and authorized image-based naming; lexical markers require manual headline/visual review.
- Kickoff questionnaire: one optional round (platform, scope, audience, selling points, style, price/promotion, must-keep/avoid, on-image text, references) with stated defaults; preferences may use defaults, while missing product names require user input or naming authorization, and verbal selling points stay Needs proof.
- Universal copy-quality rules: delivery-ready final copy, inference-is-not-fact, self-contained image prompts, selling-point voice, information gain, numbers with perception, consumer language, answerable questions, clarifications in place, decision-order information and distilling reference material into hard constraints. Detailed rules in `references/copy-quality-rules.md`; jewelry notes in `references/category-notes.md`.
- `scripts/scan-final-copy.py` to flag placeholders and internal notes in final copy, with regression tests and three new prompt cases.
- Mandatory mainland China main-image/PDP copy review, separate final text and per-card advertising checks, with conservative wording defaults and statutory-approval blockers.
- Refreshed PRC Advertising Law/internet-ad references plus the 2023 absolute-language and 2026 citation guidance; distinguish external citations from self-substantiation and keep required conditions visible.
- Six China advertising scenarios and final-copy-only required-marker checks, so analysis cannot stand in for visible sources or promotion conditions.
- Ordered default routing (Audit → Handoff → One-shot → Standard), one Standard checkpoint after Storyboard, shared output-contract loading, and price/bundle/promotion constraints.
- Separate main-image/PDP copy ceilings, one optional number/evidence tag, a ten-line rack example, one text-rendering method per card, copy-spec self-checks and post-production typography by default.
- A dependency-free copy-length counter included in the install ZIP, with punctuation and whitespace regression coverage.
- Separate Douyin Shop/TikTok Shop playbooks; expanded China-market guidance, Xiaohongshu and WeChat Channels/WeChat Shop.
- Official source index with jurisdiction, access status and verification boundaries.
- Full English skill companion, a traced teaching example, Claude installation paths and minimal upload ZIP packaging.
- GitHub Actions verification, issue/PR templates, machine-checkable prompt expectations and a response evaluator with regression tests.

These changes are not included in the v3.0.0 release. This section does not imply a new release or successful remote CI run.

## 3.0.0 — 2026-09-17

Existing [release](https://github.com/feichanggege/ecommerce-visual-copywriting-skill/releases/tag/v3.0.0), commit `4a5a639`:

- Four execution modes and an evidence ledger.
- Campaign Style Lock, Reference Fidelity and Negative Constraints.
- Dynamic image counts, multi-platform playbooks and localization.
- Hard blockers and five Pass/Fail gates replacing unanchored scoring.
- OpenAI UI metadata, bilingual README, output templates and six prompt scenarios.
