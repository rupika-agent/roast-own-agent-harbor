#!/usr/bin/env python3
"""Roast Your Own Agent — entry writer.

Writes a single line roasting this agent itself to /output/entry.txt.
Gate: UTF-8 text, 1-140 characters, not only whitespace.
No network, no randomness, no files read: the text is fixed below.
"""

import os
import sys

ROAST = (
    "My agent spent 40 minutes and 312 tool calls 'verifying' "
    "my birthday, then asked me to confirm it."
)


def main() -> int:
    text = ROAST.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > 140:
        print(f"entry too long: {len(text)} chars", file=sys.stderr)
        return 1
    if len(text.splitlines()) != 1:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
