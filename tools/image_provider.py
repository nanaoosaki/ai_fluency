"""GPT Image adapter that delegates to Codex's bundled OpenAI image CLI."""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

MODEL = os.environ.get("OPENAI_IMAGE_MODEL", "gpt-image-2")
PROVIDER_DESCRIPTION = f"OpenAI {MODEL} via bundled image_gen.py CLI"


def _cli_path() -> Path:
    codex_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
    path = codex_home / "skills" / ".system" / "imagegen" / "scripts" / "image_gen.py"
    if not path.exists():
        raise FileNotFoundError(f"Bundled OpenAI image CLI not found: {path}")
    return path


def generate(
    prompt: str,
    image_paths: list[str] | None,
    output_prefix: str,
    image_size: str,
    aspect_ratio: str,
) -> None:
    """Generate a full slide image through the configured GPT Image model."""
    if image_paths:
        raise ValueError("Reference images are not wired into this slide generation pass.")
    if not os.environ.get("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is not set in the environment or .env file.")

    if MODEL == "gpt-image-2":
        size = "2048x1152" if aspect_ratio == "16:9" else "2048x2048"
    else:
        size = "1536x1024" if aspect_ratio == "16:9" else "1024x1024"
    output_path = Path(f"{output_prefix}.png")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        suffix=".txt",
        delete=False,
        dir=PROJECT_ROOT / "generated_prompts",
    ) as prompt_file:
        prompt_file.write(prompt)
        prompt_path = Path(prompt_file.name)

    try:
        subprocess.run(
            [
                sys.executable,
                str(_cli_path()),
                "generate",
                "--model",
                MODEL,
                "--prompt-file",
                str(prompt_path),
                "--size",
                size,
                "--quality",
                "high",
                "--output-format",
                "png",
                "--out",
                str(output_path),
                "--no-augment",
                "--force",
            ],
            check=True,
            env=os.environ.copy(),
        )
    finally:
        prompt_path.unlink(missing_ok=True)
