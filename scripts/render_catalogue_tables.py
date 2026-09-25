#!/usr/bin/env python3
"""Render catalogue comparison tables as ink/paper figures for Medium."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "catalogue" / "assets"

INK = (10, 10, 10)
PAPER = (250, 250, 250)
MUTE = (80, 80, 80)

BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
if not Path(BOLD).exists():
    BOLD = "/System/Library/Fonts/Supplemental/Arial.ttf"
REGULAR = "/System/Library/Fonts/Supplemental/Arial.ttf"
MONO = "/System/Library/Fonts/Supplemental/Courier New.ttf"


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, width: int) -> list[str]:
    words = text.split()
    if not words:
        return [""]
    lines: list[str] = []
    current = words[0]
    for word in words[1:]:
        trial = f"{current} {word}"
        if draw.textlength(trial, font=fnt) <= width:
            current = trial
        else:
            lines.append(current)
            current = word
    lines.append(current)
    return lines


def render_table(
    path: Path,
    headers: list[str],
    rows: list[list[str]],
    col_weights: list[float],
    *,
    fill_header: bool = True,
    highlight_row: int | None = None,
    scale: int = 2,
) -> None:
    pad_x = 22
    pad_y = 16
    gap = 14
    header_size = 15
    body_size = 14
    line_gap = 5
    border = 2
    margin = 28

    # Measure at 1x then scale up for crisp export
    measure = Image.new("RGB", (10, 10), PAPER)
    mdraw = ImageDraw.Draw(measure)
    f_header = font(BOLD, header_size)
    f_body = font(REGULAR, body_size)
    f_body_bold = font(BOLD, body_size)

    total_weight = sum(col_weights)
    # provisional content width; refine after measuring longest wrapped content needs
    base_content_w = 920

    def col_widths(content_w: int) -> list[int]:
        return [int(content_w * w / total_weight) for w in col_weights]

    def cell_lines(text: str, fnt: ImageFont.FreeTypeFont, col_w: int, bold_first: bool = False) -> list[tuple[str, ImageFont.FreeTypeFont]]:
        # Support **bold** markers on first token only via simple strip of markdown
        clean = text.replace("**", "")
        use = f_body_bold if bold_first and text.startswith("**") else fnt
        wrapped = wrap(mdraw, clean, use, col_w - 2 * pad_x)
        return [(line, use) for line in wrapped]

    # First pass: estimate row heights with base width
    widths = col_widths(base_content_w)
    row_heights: list[int] = []

    header_line_sets = [
        wrap(mdraw, h, f_header, widths[i] - 2 * pad_x) for i, h in enumerate(headers)
    ]
    header_h = max(len(lines) for lines in header_line_sets) * (header_size + line_gap) - line_gap + 2 * pad_y
    row_heights.append(header_h)

    parsed_rows: list[list[list[tuple[str, ImageFont.FreeTypeFont]]]] = []
    for row in rows:
        cells = []
        heights = []
        for i, cell in enumerate(row):
            bold_first = cell.startswith("**")
            lines = cell_lines(cell, f_body, widths[i], bold_first=bold_first)
            cells.append(lines)
            heights.append(len(lines) * (body_size + line_gap) - line_gap + 2 * pad_y)
        parsed_rows.append(cells)
        row_heights.append(max(heights))

    table_w = base_content_w + border
    table_h = sum(row_heights) + border * (len(row_heights) + 1) // 1
    # recount borders: top + between + bottom = n_rows + 1
    table_h = sum(row_heights) + border * (len(row_heights) + 1)

    img_w = table_w + 2 * margin
    img_h = table_h + 2 * margin
    img = Image.new("RGB", (img_w, img_h), PAPER)
    draw = ImageDraw.Draw(img)

    # subtle paper grain
    for y in range(0, img_h, 4):
        for x in range(0, img_w, 4):
            if (x + y) % 8 == 0:
                draw.point((x, y), fill=(242, 242, 242))

    x0, y0 = margin, margin
    draw.rectangle(
        [x0, y0, x0 + table_w - 1, y0 + table_h - 1],
        outline=INK,
        width=border,
    )

    y = y0 + border
    all_rows: list[tuple[list, int, bool]] = [(header_line_sets, header_h, True)] + [
        (parsed_rows[i], row_heights[i + 1], False) for i in range(len(parsed_rows))
    ]

    for r_index, (cell_data, rh, is_header) in enumerate(all_rows):
        # horizontal rule above body rows already drawn via cell backgrounds; draw divider
        if r_index > 0:
            draw.line([(x0, y), (x0 + table_w - 1, y)], fill=INK, width=border)

        filled = (is_header and fill_header) or (
            highlight_row is not None and not is_header and r_index - 1 == highlight_row
        )
        if filled:
            draw.rectangle(
                [x0 + border, y, x0 + table_w - 1 - border, y + rh],
                fill=INK,
            )

        x = x0
        for c_index, width in enumerate(widths):
            if c_index > 0:
                draw.line([(x, y), (x, y + rh)], fill=PAPER if filled else INK, width=1)

            text_color = PAPER if filled else INK
            cx = x + pad_x
            if is_header:
                lines = cell_data[c_index]
                ty = y + pad_y
                for line in lines:
                    draw.text((cx, ty), line, font=f_header, fill=text_color)
                    ty += header_size + line_gap
            else:
                lines = cell_data[c_index]
                ty = y + pad_y
                for line, fnt in lines:
                    draw.text((cx, ty), line, font=fnt, fill=text_color)
                    ty += body_size + line_gap

            x += width

        y += rh

    # final bottom already from outer rect; redraw outer for crispness
    draw.rectangle(
        [x0, y0, x0 + table_w - 1, y0 + table_h - 1],
        outline=INK,
        width=border,
    )

    # L-bracket ticks (brand motif)
    tick = 12
    draw.line([(x0, y0), (x0 + tick, y0)], fill=INK, width=border)
    draw.line([(x0, y0), (x0, y0 + tick)], fill=INK, width=border)
    draw.line(
        [(x0 + table_w - 1, y0 + table_h - 1), (x0 + table_w - 1 - tick, y0 + table_h - 1)],
        fill=INK,
        width=border,
    )
    draw.line(
        [(x0 + table_w - 1, y0 + table_h - 1), (x0 + table_w - 1, y0 + table_h - 1 - tick)],
        fill=INK,
        width=border,
    )

    if scale != 1:
        img = img.resize((img_w * scale, img_h * scale), Image.Resampling.NEAREST)

    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, "PNG")
    print(f"Wrote {path.relative_to(ROOT)} ({img.size[0]}x{img.size[1]})")


def main() -> None:
    render_table(
        OUT / "02-scenario-stage-map.png",
        ["Scenario", "Primary stage", "Key technique", "What you buy"],
        [
            [
                "Hierarchical search",
                "Retrieval + presentation",
                "Progressive disclosure, compact encoding",
                "Growth bounded by branching factor",
            ],
            [
                "Corpus RAG",
                "Filtration",
                "Filtration chain or sub-agent",
                "Large token cut (measure yours)",
            ],
            [
                "Tabular analysis",
                "Eviction",
                "Offload + scripting",
                "Orders-of-magnitude reduction",
            ],
        ],
        [1.15, 1.2, 1.45, 1.35],
    )

    render_table(
        OUT / "03-layers-progress.png",
        ["Layer", "Question it answers", "Progress belongs here?"],
        [
            [
                "**Context**",
                "What tokens does the model attend to on the next call?",
                "No — unless a specific status line is load-bearing for the next decision",
            ],
            [
                "**State**",
                "What durable facts does the runtime remember (IDs, pointers, checkpoints)?",
                "Only as pointers or counters if something later must act on them—not as a narrative dump",
            ],
            [
                "**Flow**",
                "How does an event escape a tool or subagent to a consumer inside the process?",
                "Yes — this is the side channel’s core",
            ],
            [
                "**Protocol**",
                "How are events typed and serialized for a given consumer contract?",
                "At the edge, after flow",
            ],
            [
                "**Transport**",
                "How do bytes move (SSE, WebSocket, queue broker, gRPC)?",
                "At the edge, after protocol",
            ],
        ],
        [0.85, 1.7, 1.7],
        highlight_row=2,
    )

    render_table(
        OUT / "04-picking-patterns.png",
        ["Situation", "Lean toward"],
        [
            [
                "High reject rate, cheap gate, happy-path latency acceptable",
                "Precondition gating (blocking)",
            ],
            [
                "Low reject rate, gate latency hurts the p50",
                "Optimistic execution—if you can cancel cleanly",
            ],
            [
                "Exit must be a traced decision the model makes",
                "Terminal tool",
            ],
            [
                "Exit rides alongside structured content every turn",
                "Control flag",
            ],
            [
                "Hard SLO / runaway protection",
                "Budget exit (always)",
            ],
            [
                "Answers are comparable; adaptive compute helps",
                "Self-consistency early stop",
            ],
            [
                "Parallel tactics, first success wins",
                "Disjunctive cancel (resolved / scoped group)",
            ],
            [
                "Any branch can veto the whole run",
                "Conjunction-break (workflow)",
            ],
            [
                "Concurrent peers would recompute the same key",
                "Singleflight",
            ],
        ],
        [1.55, 1.25],
    )


if __name__ == "__main__":
    main()
