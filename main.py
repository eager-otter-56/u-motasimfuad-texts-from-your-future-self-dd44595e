#!/usr/bin/env python3
"""Texts From Your Future Self — entry writer.

Writes the future-self text message to entry.txt in MAKEFUN_OUTPUT_DIR
(default /output). Gate: UTF-8 text, 1-200 characters, not only whitespace.
"""

import os
import stat

ENTRY_TEXT = (
    "hey, it's you from next tuesday. i just read all 5,271 messages "
    "you sent yourself about finishing this and replied to every one. "
    "you're still not done. neither am i."
)
"""The text is the message as it would arrive: no setup, no context."""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY_TEXT
    # Gate assertion: 1-200 characters, not only whitespace, single line.
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of gate"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
