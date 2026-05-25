#!/usr/bin/env python3
"""Compile full-slide image prompts and optionally render them.

The storyboard commits the wording first; each image prompt then asks the
selected image model to render a complete presentation slide.
"""

from __future__ import annotations

import argparse
import importlib
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

PROMPT_DIR = PROJECT_ROOT / "visual_prompts"
GUIDELINE_PATH = PROJECT_ROOT / "visual_guideline.md"
COMPILED_DIR = PROJECT_ROOT / "generated_prompts"
VISUAL_DIR = PROJECT_ROOT / "generated_slides"


def select_prompt_files(slides: list[int] | None) -> list[Path]:
    """Return prompt files in slide order, optionally filtered by number."""
    prompt_files = sorted(PROMPT_DIR.glob("slide_*.md"))
    if not slides:
        return prompt_files

    selected = set(slides)
    return [
        path
        for path in prompt_files
        if (match := re.search(r"slide_(\d+)", path.stem))
        and int(match.group(1)) in selected
    ]


def slide_number(path: Path) -> int:
    """Extract a numeric slide id from a visual prompt filename."""
    match = re.search(r"slide_(\d+)", path.stem)
    if not match:
        raise ValueError(f"Prompt filename does not contain a slide number: {path.name}")
    return int(match.group(1))


def compile_prompt(prompt_path: Path, guideline: str) -> str:
    """Assemble a reviewed, provider-ready visual prompt."""
    slide_brief = prompt_path.read_text(encoding="utf-8").strip()
    return f"""You are generating one complete 16:9 slide for a live HTML5 presentation.

NON-NEGOTIABLE OUTPUT CONTRACT:
- Render a full finished slide image, including the supplied exact text.
- Preserve the exact wording, spelling, punctuation, capitalization, and filename syntax.
- Do not add any words, labels, logos, watermarks, or pseudo-text beyond the supplied copy.
- Prioritize large, projection-readable typography over decorative detail.

VISUAL GUIDELINE:
{guideline}

SLIDE VISUAL BRIEF:
{slide_brief}
"""


def export_prompt(prompt_path: Path, guideline: str) -> tuple[int, Path, str]:
    """Compile and write one prompt for inspection or external generation."""
    number = slide_number(prompt_path)
    compiled = compile_prompt(prompt_path, guideline)
    output_path = COMPILED_DIR / f"slide_{number:02d}_prompt.txt"
    output_path.write_text(compiled, encoding="utf-8")
    return number, output_path, compiled


def render_visual(
    number: int,
    prompt: str,
    provider_module: str,
    image_size: str,
) -> None:
    """Render one complete generated slide through the selected adapter."""
    provider = importlib.import_module(provider_module)
    output_prefix = str(VISUAL_DIR / f"slide_{number:02d}")
    provider.generate(
        prompt=prompt,
        image_paths=None,
        output_prefix=output_prefix,
        image_size=image_size,
        aspect_ratio="16:9",
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compile full-slide prompts and optionally generate slide images."
    )
    parser.add_argument("--slides", type=int, nargs="+", help="Specific slide numbers to process.")
    parser.add_argument(
        "--render",
        action="store_true",
        help="Render generated slides after exporting prompts. Without this flag, no model is called.",
    )
    parser.add_argument(
        "--provider-module",
        default="tools.image_provider",
        help="Python module exposing generate(...). Defaults to the swappable adapter.",
    )
    parser.add_argument("--size", default="1K", help="Provider image size argument.")
    parser.add_argument("--workers", type=int, default=1, help="Concurrent render workers.")
    args = parser.parse_args()

    guideline = GUIDELINE_PATH.read_text(encoding="utf-8")
    prompt_files = select_prompt_files(args.slides)
    if not prompt_files:
        raise SystemExit("No visual prompt files matched the requested slides.")

    COMPILED_DIR.mkdir(exist_ok=True)
    VISUAL_DIR.mkdir(exist_ok=True)

    exports = [export_prompt(path, guideline) for path in prompt_files]
    for number, output_path, _ in exports:
        print(f"Exported slide {number:02d} prompt -> {output_path.relative_to(PROJECT_ROOT)}")

    if not args.render:
        print("Prompt export complete. No image provider was called.")
        return

    max_workers = max(1, args.workers)
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(render_visual, number, prompt, args.provider_module, args.size)
            for number, _, prompt in exports
        ]
        for future in futures:
            future.result()

    print("Generated slide rendering complete.")


if __name__ == "__main__":
    main()
