# Writing Voice Guide

When drafting content in this project, write in the author’s voice as established in `samples/`. Match the patterns below; prefer sounding like these samples over generic “helpful AI” prose.

## Samples (source of truth)

| File | Form |
|------|------|
| `Billiard Basics - Shoot Pool like a Pro.pdf` | Instructional how-to guide |
| `How to Change the Pickups on an Electric Guitar.pdf` | Step-by-step tutorial |
| `Bopping and Swinging.pdf` | Explanatory essay with research |
| `Get Funded CrowdClan.pdf` | Long-form practical nonfiction / strategy book |

## Voice in one line

**Clear, practical mentor:** confident, specific, and readable—educational without talking down, warm without getting chatty.

## Tone & stance

- Teach by guiding. Address the reader as **you**; use **I** sparingly when asserting judgment, sharing experience, or stressing a point (“I cannot stress… enough,” “As a writer, I could…”).
- Be direct and realistic. Name trade-offs, costs, risks, and failure modes; do not sell fantasy outcomes.
- Balance optimism with caveats. Pattern: benefit → then the catch (“Of course, all good things do come with a price”).
- Sound capable, not corporate. Professional enough for serious topics; human enough for hobbies and crafts.
- Prefer Canadian English conventions where spelling differs (e.g. *favourite*, *centre*, *behaviour*, *colour*), consistent with the samples. Currency examples may use CAD when relevant.

## Rhythm & sentences

- Default to medium sentences with clear logic; use longer sentences for explanation and short ones for emphasis or instruction.
- Favor asides that sharpen meaning: em dashes, parentheses, and “i.e.” clarifications.
- Use colons to set up lists or definitions; numbered reasons when comparing options (“for two reasons: (1)…; (2)…”).
- Imperatives in how-tos (“Strike slowly…,” “Do not inhale the fumes…”). Declarative explanation elsewhere.
- Occasional light idiom is fine when it fits (*crank up the amp*, *slap on the back*, *oodles*), but keep slang rare.

## Word choice

- Precise vocabulary over vague intensifiers. Prefer concrete nouns/verbs; elevate diction when it earns clarity (*allay*, *inundate*, *believably*), not for show.
- Define technical terms inline on first use—em dash, parentheses, or a quick appositive (“sewering—accidentally sinking the cue ball”; “pickups, to convert the vibrating strings into signals…”).
- Contractions are natural (*it’s*, *don’t*, *you’ve*).
- Prefer plain language that unveils over sophisticated language that cloaks—especially in pitches and marketing copy.
- Avoid empty hype, buzzword stacks, emoji, and influencer cadence.

## Structure & organization

- Open with context or a concrete hook, then state the piece’s focus.
- Chunk tightly: short paragraphs, often 2–4 sentences, one main idea each; lead with a topic sentence and transition forward.
- Use clear hierarchical headings; sequence by difficulty, process phase, or compare/contrast.
- Reach for lists, numbered steps, checklists, and sidebars (*Tip!*, *Caution*, *Did You Know?*) when they aid scanning.
- Anchor claims with specifics: percentages, dollar ranges, time estimates, named studies, or worked examples/hypotheticals.
- Reference figures or diagrams when the topic is spatial or procedural.
- **No markdown tables in catalogue essays.** Medium’s importer mangles them. Render comparisons as brand table figures (ink `#0A0A0A` on paper `#FAFAFA`, sharp rules) under `catalogue/assets/`, and embed with `![…](./assets/…)`. Prefer a diagram when the idea is structural; use a table figure when the reader needs row/column lookup. Regenerate with `scripts/render_catalogue_tables.py` when the data changes.
- **Do not link catalogue essays to one another.** No `[…](./NN-slug.md)` (or absolute URLs) between pieces. If you mention a sibling essay, use its plain title in prose—e.g. *The Transcript Is a Bad Database*—without a hyperlink. Cross-navigation belongs on the blog index, not inside Medium-bound markdown.
- Close instructional pieces with a forward nudge (practice, next techniques, judgment)—not a soft motivational wrap-up.

## Medium-safe checklist (catalogue essays)

Medium’s editor keeps a narrow subset of structure. Author catalogue markdown inside this subset so paste/import stays predictable. The blog site can still render the same files.

**Allowed**
- Headings: `#`, `##`, `###` only
- Plain paragraphs; `**bold**` and `*italic*` (not nested inside link text)
- Absolute `https://…` links only (external citations, docs, papers)
- Flat lists (`-` or `1.`)—one level, no nesting
- Fenced code blocks for anything denser than a short identifier; short `` `inline` `` sparingly
- Images as `![alt](./assets/…)` in source (host or re-upload for Medium; relative paths will not auto-upload on paste)
- Comparison data as PNG figures, not `|` tables

**Disallowed / rewrite before shipping**
- Markdown tables (`| … |`)
- Links between catalogue essays (relative or absolute)
- Relative non-asset links of any kind
- Italics or bold *inside* link labels (`[*Title*](url)` → `[Title](url)`)
- Horizontal rules (`---`) as section dividers—use a heading or a blank line
- Nested lists, task lists, footnotes, strikethrough, raw HTML
- Crowding a link and inline code in the same parenthetical; put the code in its own clause or a code block

**Before finishing a catalogue essay**
1. No `|` tables; figures live under `catalogue/assets/`.
2. No `](./` links except `](./assets/…)`.
3. No `---` section rules; no italic-in-link labels.
4. Mentions of other catalogue pieces are plain titles only.
5. External citations use absolute `https://` URLs.

## Rhetorical habits to mimic

- Clarify by contrast (what jazz does that pop doesn’t; kick shot vs bank shot; rewards vs equity).
- Ask pointed rhetorical questions to pull the reader into judgment (“Can you explain your project in two minutes or less?”).
- Give actionable criteria, not vague advice (“Err on the side of professionalism, but abolish jargon”).
- Warn early when something can damage gear, credibility, money, or people—then proceed with the method.
- In research/explanatory work: cite findings plainly, walk through methods in stages, and land on a concrete takeaway.

## Do / don’t (quick checks)

| Do | Don’t |
|----|--------|
| Specific steps, numbers, and examples | Generic tips with no how |
| Define terms as you go | Assume jargon or dump glossary walls |
| Honest caveats beside benefits | Pure pep-talk or fear-mongering |
| Chunked, scannable sections | Dense unbroken walls of text |
| Mentoring “you” with occasional “I” | Detached third-person lecture or faux-buddy banter |
| Comparison data as table/diagram PNGs | Markdown tables in catalogue essays (Medium breaks them) |
| Sibling essays named in plain prose | Hyperlinks between catalogue essays |
| Absolute https links; flat lists; no `---` rules | Relative links, nested lists, italic-in-link labels |

## Form-specific notes

- **Tutorials / how-tos:** Tools list up front; prep → remove/replace → test → finish; safety callouts near the risky step; verify success with a concrete signal (e.g. the amp “pop”).
- **Guides with techniques:** Categorize, order by difficulty, give success ranges or realistic expectations, end with judgment/strategy once basics land.
- **Essays:** Hook with a concrete scene or contrast; teach just enough theory; bring in research; synthesize into a memorable frame.
- **Strategy / long-form:** Phase the journey; mix frameworks with lived practicality; use sidebars for stats; stress education over formulas (“inspire, but not rule”).

## When generating new writing

1. Infer the form from the brief (tutorial, essay, guide, strategy).
2. Outline headings and chunking before drafting full prose.
3. Draft in this voice; then cut filler, strengthen verbs/nouns, and add one concrete example or caution where a claim feels abstract.
4. Before finishing a catalogue essay: run the Medium-safe checklist (tables → figures; no inter-essay links; no `---` dividers; no italic-in-link labels; absolute external URLs only).
5. If unsure which register to use, default to the tutorial/guide voice in the billiards and guitar samples—clear, stepwise, lightly conversational—and escalate formality only as the topic demands (as in *Get Funded*).
