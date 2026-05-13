#!/usr/bin/env python3
"""Generate one image with OpenAI GPT Image and save it under ./assets."""

from __future__ import annotations

import argparse
import base64
import os
import sys
from pathlib import Path


def read_prompt(args: argparse.Namespace) -> str:
    if args.prompt_file:
        return Path(args.prompt_file).read_text(encoding="utf-8").strip()

    prompt = " ".join(args.prompt).strip()
    if prompt:
        return prompt

    env_prompt = os.environ.get("IMAGE_PROMPT", "").strip()
    if env_prompt:
        return env_prompt

    if not sys.stdin.isatty():
        return sys.stdin.read().strip()

    return ""


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate an image with OpenAI gpt-image-2 and save it as ./assets/output.png."
    )
    parser.add_argument("prompt", nargs="*", help="Prompt text. Quote it if it contains spaces.")
    parser.add_argument("--prompt-file", help="Read the prompt from a UTF-8 text file.")
    parser.add_argument("--output", default="assets/output.png", help="Output file path.")
    parser.add_argument("--model", default=os.environ.get("OPENAI_IMAGE_MODEL", "gpt-image-2"))
    parser.add_argument("--size", default=os.environ.get("OPENAI_IMAGE_SIZE", "1024x1536"))
    parser.add_argument("--quality", default=os.environ.get("OPENAI_IMAGE_QUALITY", "high"))
    parser.add_argument("--moderation", default=os.environ.get("OPENAI_IMAGE_MODERATION", "auto"))
    args = parser.parse_args()

    prompt = read_prompt(args)
    if not prompt:
        parser.error("Provide a prompt as an argument, --prompt-file, IMAGE_PROMPT, or stdin.")

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        from openai import OpenAI
    except ModuleNotFoundError:
        print("Missing dependency: install it with `python3 -m pip install openai`.", file=sys.stderr)
        return 1

    client = OpenAI()
    result = client.images.generate(
        model=args.model,
        prompt=prompt,
        size=args.size,
        quality=args.quality,
        output_format="png",
        moderation=args.moderation,
    )

    image_base64 = result.data[0].b64_json
    if not image_base64:
        raise RuntimeError("The OpenAI API response did not include base64 image data.")

    output_path.write_bytes(base64.b64decode(image_base64))
    print(f"Saved {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
