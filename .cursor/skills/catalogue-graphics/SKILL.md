---
name: catalogue-graphics
description: >-
  Generate catalogue article graphics in the project brand: black/white utility
  brutalism with Canadian English. Use when creating hero/header images for
  socials, Open Graph cards, in-article diagrams, concept figures, or any visual
  assets for catalogue essays—or when the user mentions brand graphics, article
  illustrations, or social thumbnails.
---

# Catalogue graphics

## Before every generation

1. **Read both reference images** with the Read tool (vision)—do not skip:
   - [references/hero-og.png](references/hero-og.png) — social / hero
   - [references/diagram.png](references/diagram.png) — in-article diagram
2. Match their density, stroke weight, typography, and motif energy—not a sparser remake.
3. Write outputs into the workspace. Copy from Cursor assets folders into the project if generation lands outside the repo.

## Brand in one line

**Utility brutalism with life:** high contrast, hard edges, functional motifs—accessible and scannable, never empty or corporate-decorative.

## Palette

| Token | Hex | Use |
|-------|-----|-----|
| Ink | `#0A0A0A` | Text, rules, fills, arrows |
| Paper | `#FAFAFA` | Background (off-white; subtle paper grain OK) |
| Mute | `#6B6B6B` | Avoid when possible; prefer lighter **weight** of ink for secondary labels |

No accent colours. No gradients, glow, soft shadows, or blur. Contrast ≥ 4.5:1 for all text.

## Type & copy

- Geometric grotesque / sharp sans; bold for stage names and headlines; regular or mono-feel for captions.
- **Canadian English** only (`colour`, `centre`, `behaviour`, `favourite`, `catalogue` as a word in prose—not as a brand chrome).
- Literal labels that name the idea (`RETRIEVE`, `CLAIM CHECK`, `inc-vpn`)—not metaphor art.
- **Never** include: site/wordmark chrome, the word `CATALOGUE` as branding, article numbers (`01`), or footer page indices.

## Layout grammar

- Sharp corners (0–2px). Hairline or 2px rules; consistent stroke weight in a piece.
- Mix **solid fills and outlines** for rhythm (this is the “life”).
- Hard grid, generous but intentional negative space—not sparse emptiness.
- No soft UI cards, pill clusters, emoji, stock photos, or “AI glow.”

## Two asset types only

### 1. Hero / social (`references/hero-og.png`)

- Aspect: **16:9** for OG (also generate **1:1** when asked for square socials).
- Big article title + one short supporting line.
- Asymmetric energy: typographic mass + a **dense functional motif** (crowded window vs clean claim-check, etc.).
- Architectural ticks, L-brackets, chunky arrows OK.

### 2. In-article diagram (`references/diagram.png`)

- **Diagram only**—no title band, subtitle, section header, or surrounding tile/card chrome. The image *is* the figure.
- Stages or relationships with motifs *inside* the idea (tree, funnel strokes, grid, fill→outline)—not four identical empty boxes.
- Chunky arrows; labels and short captions on the stages themselves.
- Crop tight to the diagram.

## When to make a graphic

- **Yes:** hard-to-hold structure (lifecycles, failure modes, contrasts like stuffing vs pointer).
- **Yes:** one hero per article for socials.
- **Yes:** comparison / lookup tables that would otherwise be markdown `|` tables—Medium mangles those. Render as ink/paper table figures (see `scripts/render_catalogue_tables.py`) or as a structural diagram when the idea is relational rather than tabular.
- **No:** decorative fillers, repeated motifs that don’t teach.

## Generation checklist

- [ ] Reference images read this session
- [ ] Canadian spelling; no catalogue chrome / article numbers
- [ ] Hero has title life; diagram is figure-only
- [ ] Monochrome ink/paper; sharp; fills + outlines
- [ ] File saved under the project path the user can open
