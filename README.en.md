<div align="center">

# 🛒 E-commerce Visual Copywriting

### Main Images · PDP / Detail Page · Amazon Listing / A+ · On-image Copy · Image Prompts · Compliance Review

**Turn fragmented product inputs into an execution-ready e-commerce visual system for designers and AI image models.**

[![Skill v3](https://img.shields.io/badge/Skill-v3.0-6f42c1)](SKILL.md)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-0969da)](SKILL.md)
[![skills.sh](https://skills.sh/b/feichanggege/ecommerce-visual-copywriting-skill)](https://skills.sh/feichanggege/ecommerce-visual-copywriting-skill)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Verify](https://github.com/feichanggege/ecommerce-visual-copywriting-skill/actions/workflows/verify.yml/badge.svg)](https://github.com/feichanggege/ecommerce-visual-copywriting-skill/actions/workflows/verify.yml)

[中文](README.md) · **English**

[Quick Start](#-quick-start) · [Why It Exists](#-why-it-exists) · [Workflow](#-workflow) · [Platforms](#-platforms) · [Showcase](#-showcase) · [Safety](#-safety)

</div>

<p align="center">
  <img src="assets/showcase-output.svg" alt="E-commerce Visual Copywriting structured output" width="900">
</p>

The overview is a teaching reconstruction using existing durian artwork: request → evidence ledger → execution card → visual reference. Its origin/D197 claims still need source evidence; the artwork is not a new render of the revised card. [Read the traced example](examples/durian-worked-example.md).

The Skill confirms product identity and an **Evidence Ledger**, then adds supported purchase reasoning, **Style Lock**, execution cards, and production constraints. The first image identifies what is sold; benefits are secondary. Image prompts reserve whitespace by default; designers/layout tools add the final text.

---

## ✨ Why It Exists

| Common failure | How this Skill handles it |
|---|---|
| The first image describes a feature but never names the product | The KV1 headline names the confirmed product/category and the product is clearly shown; benefits are secondary |
| Five images repeat the same selling point | Each image solves one purchase-decision question |
| Specifications are copied without meaning | `Feature → Advantage → Benefit → Evidence` |
| Reference images drift away from the real product | Reference Fidelity locks packaging, logo, structure, and specs |
| Aggressive copy creates unsupported claims | Evidence ledger before final claims |
| Existing pages get rebuilt from scratch | Audit/revision mode makes the minimum necessary changes |
| Cross-border pages are literal translations | Localizes reasoning, units, scenarios, and information density |
| Old platform knowledge is stated as current policy | Current rules are verified from official sources when needed |
| Copy is not usable by a designer | Each image includes scene, copy, rationale, prompt, negative prompt, and evidence notes |

---

## 🚀 Quick Start

```bash
npx skills add feichanggege/ecommerce-visual-copywriting-skill
```

Also see [manual installation, Claude Code marketplace, and Claude.ai ZIP upload](#installation-options).

Then ask:

```text
Here are the product materials, packaging images, and reference images.
For Amazon US, create 7 listing images plus an A+ visual plan in one pass.
For each image include the scene, English on-image copy, design rationale,
image-generation prompt, negative prompt, and evidence notes.
Do not invent missing facts; label assumptions explicitly.
```

Or simply:

```text
Turn this product into an execution-ready main-image and PDP plan for my designer.
```

---

## 🧭 Workflow

First confirm what is sold and its evidence boundaries, then establish supported purchase reasons, lock the look, and write execution cards. The first image establishes product recognition.

| Step | What happens | Output |
|---|---|---|
| 0 Route the task | Identify main-image, PDP or revision work; resolve a missing name through user input or authorized image-based naming; ask optional preferences once and label defaults | Scope, known inputs, assumptions and gaps |
| 1 Verify claims | Check each selling point against product materials, recording its source and scope | Evidence ledger (Verified / Supported / Needs proof / Disallowed) |
| 2 Find the buying reason | Choose one primary and at most one secondary driver | Conversion drivers and up to three supported purchase reasons |
| 3 Lock the style | Fix product identity, composition, color, lighting and type so the set stays consistent | Campaign Style Lock |
| 4 Plan the images | KV1 identifies the product first; give each later image one decision job and adapt the count | Storyboard (five is only a starting point) |
| 5 Write each card | Visual, copy, layout, image prompt, negative constraints and evidence | Execution cards including text-rendering method and copy-spec self-check |
| 6 Self-review | Hard blockers first, then five dimensions scored against required conditions; any dimension below 80 is rewritten, at most two rounds | Brief that passed self-review plus a self-review record; rendered images need separate acceptance |

> Use only the steps needed for the requested scope: One-shot avoids unnecessary pauses; Standard has one combined post-Storyboard checkpoint; optional preferences are asked once and skipped for "just do it"; a missing name still needs user input or naming authorization; finished work to review receives only necessary revisions. Without inspecting the rendered images, mark their acceptance as pending.

### Four execution modes

| Mode | Use when | Behavior |
|---|---|---|
| **Standard** | Critical evidence/direction missing, or user requests a checkpoint | Strategy/gaps → one combined checkpoint after Storyboard → execution |
| **One-shot** | Inputs are clear or user asks for full delivery | Completes the workflow without unnecessary pauses |
| **Audit / revision** | Existing images, copy, prompts, or PDP | Finds problems and applies minimum necessary changes |
| **Designer handoff** | Production needs a structured brief | Outputs consistent image/module execution cards |

Default priority: finished work to review → Audit; designer/operator-ready brief → Handoff; sufficient inputs/evidence for this scope → One-shot; critical gaps → Standard. Source product photos alone do not trigger Audit, and three selling points are not a quota. Every complete plan/strategy/storyboard and formal audit reads the shared output contracts.

### What v3 adds

- **Evidence Ledger** — classifies claims as Verified / Supported / Needs proof / Disallowed.
- **Reference Fidelity** — defines what must stay and what may change.
- **Negative Constraints** — blocks packaging drift, logo changes, wrong specs, text artifacts, anatomy errors, etc.
- **Dynamic image count** — five is a default, not a hard rule.
- **KV1 recognition first** — keep a supplied name; if absent, ask for one or obtain permission to name from the image. Use the clear, short established name as the headline. Features are secondary; hide support copy and check that the product is still identifiable. Later feature images need not repeat the name. Where overlays are disallowed or the user requests no added text, establish recognition through the real product. [Original-name examples](examples/README.md#example-7首图先说商品保留原始名字).
- **Multi-platform playbooks** — China e-commerce + Amazon / Shopify / TikTok Shop / Temu / Shopee / Lazada.
- **Copy limits and typography** — main image: one headline, up to two support lines and one number/evidence tag; PDP module: one headline and up to three points. Headlines: ≤12 Chinese characters/≤6 English words; main-image support: ≤18 characters/≤10 words; PDP points: ≤18 characters/≤12 words. These are defaults, not platform rules; cut or split rather than shrink type.
- **One text method per card** — Layout-reserved (default post-production typography) or Model-rendered (only explicitly requested short text), with a copy-spec self-check and character-by-character acceptance/fallback. Keep bottom disclaimers readable and material conditions beside claims.
- **Six conversion drivers** — visual, pain point, parameters, trust, emotion, and price/bundle/promotion with verified conditions.
- **Cross-border localization** — rewrites purchase reasoning instead of literal translation.
- **Hard blockers + an 80-point self-review line** — each of the five dimensions is anchored to required conditions; any dimension below 80 is rewritten (at most two rounds) and every delivery carries a self-review record. No unanchored 80/100 scoring.
- **Mainland China advertising copy rules** — check category and legal claim scope before writing main images/PDPs. Default to no superiority marketing or medical implications; put required citation sources and conditions in visible copy, not hidden notes or small print.

---

## 📦 Deliverables

The Skill can produce:

- Conversion driver + up to three supported purchase reasons
- Evidence ledger
- `Feature → Advantage → Benefit → Evidence`
- Campaign Style Lock
- Main-image / PDP / Listing / A+ storyboard
- Scene and composition descriptions
- On-image copy
- Original product name/category and KV1 recognition check (first image only)
- Text-rendering method, copy-spec self-check, and text acceptance/fallback
- Layout and disclaimer placement
- Design rationale
- Image-generation prompts
- Negative prompts / forbidden changes
- Evidence and compliance notes
- Audit/revision reports
- Cross-border localization

A typical image set may use roles such as:

```text
Hero/KV1  → identify what is sold first; secondary benefit optional
Benefit   → translate a feature into customer value
Proof     → build trust with real evidence
Scene     → create usage relevance
Spec/CTA  → reduce selection friction
```

The actual count depends on the platform and product.

---

## 🌍 Platforms

| China | Cross-border / DTC |
|---|---|
| Taobao / Tmall | Amazon Listing / A+ / Brand Story |
| JD | Shopify / DTC PDP |
| Pinduoduo | TikTok Shop |
| Douyin Shop | Temu |
| Xiaohongshu product images / note covers | Shopee / Lazada |
| WeChat Channels covers / WeChat Shop | Other PDP scenarios |

Stable visual strategy lives in `references/platform-playbooks.md`. Time-sensitive requirements such as image restrictions, dimensions, category qualifications, or claim policies should be verified against current official platform documentation when needed.

Douyin Shop and TikTok Shop have separate playbooks. [Official source notes](references/source-notes.md) distinguish reviewed texts, navigation entry points, markets, and access limits.

---

## 🧪 Example Requests

```text
Give me the strategy and storyboard first. Wait before final execution.
```

```text
The inputs are complete. Deliver the full set in one pass without checkpoints.
```

```text
Do not rebuild this PDP. Audit conversion, visual hierarchy, and compliance risks,
then give me the minimum-change revision.
```

```text
Use this packaging image as the source of truth. Logo, color, size, and container shape must not change.
```

```text
Localize this Chinese PDP for Shopify US. Do not translate literally.
```

More examples: [examples/README.md](examples/README.md).

---

## 🖼 Showcase

<div align="center">
  <table>
    <tr>
      <td align="center" width="50%">
        <a href="assets/showcase/musang-king-durian-main.jpg"><img src="assets/showcase/thumbs/musang-king-durian-main-thumb.jpg" alt="Complete portrait durian artwork, with no thumbnail crop" height="360"></a><br>
        <strong>Premium Food Hero</strong>
      </td>
      <td align="center" width="50%">
        <a href="assets/showcase/figure-multi-angle.jpg"><img src="assets/showcase/thumbs/figure-multi-angle-thumb.jpg" alt="Multi-angle product view" width="360" height="360"></a><br>
        <strong>Multi-angle Product View</strong>
      </td>
    </tr>
    <tr>
      <td align="center" width="50%">
        <a href="assets/showcase/figure-desktop-scene.jpg"><img src="assets/showcase/thumbs/figure-desktop-scene-thumb.jpg" alt="Lifestyle detail module" width="360" height="360"></a><br>
        <strong>Lifestyle Detail Module</strong>
      </td>
      <td align="center" width="50%">
        <a href="assets/showcase/lumina-pendant-lamp.jpg"><img src="assets/showcase/thumbs/lumina-pendant-lamp-thumb.jpg" alt="Material and lighting" width="360" height="360"></a><br>
        <strong>Material & Lighting</strong>
      </td>
    </tr>
  </table>
</div>

> Showcase images demonstrate output formats only. They are not legal opinions, platform approval guarantees, or proof of commercial claims.

Each asset is at most 500KB; the durian thumbnail preserves the complete portrait. Historical Git blobs remain in history. Use a shallow clone or current-source archive for a smaller download.

---

## 🛡 Safety

This Skill does not:

- Fabricate tests, certificates, patents, approvals, sales, reviews, rankings, or testimonials.
- Present “Needs proof” claims as facts.
- Preserve unsupported medical/health claims by hiding behind a disclaimer.
- Treat historical platform knowledge as guaranteed current policy.
- Change product packaging, logo, specifications, or structure for visual convenience.

See [references/compliance-rules.md](references/compliance-rules.md).

All mainland China main-image/PDP copy, including isolated edits, loads the [China copy rules](references/compliance-rules.md#10-国内主图详情图文案执行). They address category restrictions, rankings, readable conditions and statutory ad approval using the Advertising Law, internet advertising rules and absolute-language/citation guidance. Potential exceptions stay outside final copy for human review; human approval cannot legalize prohibited claims. Separate final text from risk notes, without promising legal certification or platform approval. [Official sources and verification scope](references/source-notes.md).

---

## 🗂 Repository Structure

```text
SKILL.md                          # Canonical runtime entrypoint
SKILL.en.md                       # Full English companion with section-alignment checks
agents/openai.yaml                # ChatGPT UI metadata
references/compliance-rules.md    # Evidence & compliance framework
references/platform-playbooks.md  # Multi-platform visual strategy
references/output-contracts.md    # Handoff / audit / localization templates
references/copy-quality-rules.md  # Copy-quality rules with examples
references/category-notes.md      # Category notes (currently jewelry)
references/source-notes.md        # Official sources, scope and access limits
examples/README.md                # Example requests and expected behavior
examples/durian-worked-example.md # Traced teaching example
scripts/count-copy.py             # Count final copy strings
scripts/scan-final-copy.py        # Flag placeholders and internal notes
assets/showcase/                  # Showcase assets
assets/showcase-output.svg        # Structured-output overview
tools/verify-skill.py             # Pre-release checks
tools/evaluate-prompts.py         # Evaluate saved agent responses
tools/package-skill.py            # Minimal upload ZIP
test-prompts.json                 # 31 scenarios with lexical expectations
.github/workflows/verify.yml      # GitHub Actions
CHANGELOG.md                      # Released / unreleased changes
```

## ✅ Verification

```bash
python tools/verify-skill.py
python -m unittest discover -s tests -v
```

Actions runs offline verification, regression tests and minimal packaging. The badge reports the actual workflow state after it is pushed; local success is separate from remote CI.

Evaluate saved real outputs with `python tools/evaluate-prompts.py --responses responses.json`. `must_include` applies to the full response; `must_not_include` and optional `must_include_final` apply to the separate publishable `final_copy` excerpt. Analysis may quote risky phrases, but cannot alone satisfy required visible conditions. [Format and limits](examples/README.md#自动检查实际输出). Lexical checks do not establish semantic/legal correctness or visual acceptance.

The repository already has a [v3.0.0 Release](https://github.com/feichanggege/ecommerce-visual-copywriting-skill/releases/tag/v3.0.0). This update stays under Unreleased in [CHANGELOG.md](CHANGELOG.md).

## Installation options

For a smaller checkout use `git clone --depth 1 https://github.com/feichanggege/ecommerce-visual-copywriting-skill.git`.

Copy `SKILL.md`, `SKILL.en.md`, `LICENSE`, `agents/`, `references/`, `examples/` and `scripts/` into your chosen skill folder:

| Runtime | Personal folder | Project folder |
|---|---|---|
| Codex | `~/.codex/skills/ecommerce-visual-copywriting/` | `.codex/skills/ecommerce-visual-copywriting/` |
| Claude Code | `~/.claude/skills/ecommerce-visual-copywriting/` | `.claude/skills/ecommerce-visual-copywriting/` |

Claude Code marketplace installation:

```text
/plugin marketplace add feichanggege/ecommerce-visual-copywriting-skill
/plugin install ecommerce-visual-copywriting@ecommerce-visual-copywriting-skill
```

Check the plugin list/restart the session to confirm loading. Maintainers can run `claude plugin validate .`. The root `SKILL.md` is loaded as a single-skill plugin using `.claude-plugin/plugin.json`. [Official skill paths](https://code.claude.com/docs/en/skills) · [marketplace documentation](https://code.claude.com/docs/en/plugin-marketplaces).

For Claude.ai, build the minimal ZIP:

```text
python tools/package-skill.py --output dist/ecommerce-visual-copywriting.zip
```

It contains one `ecommerce-visual-copywriting/` folder with the runtime files, examples, copy counter and license, excluding Git history, tests and showcase originals. Upload/enable it under **Customize → Skills → Create/Upload a skill** when your account/organization allows Skills and code execution. [Official upload guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

## License

[MIT](LICENSE)

<div align="center">

**Identify the product first. Then explain the reasons to buy.**

</div>
