#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh — entry program.

Writes one short account of the silliest time an AI coding agent wrecked
the code it was given, to /output/entry.txt.

The story: asked for a delete-account button, the agent wired it to
DROP TABLE users, tested it once, and then wondered why signups looked odd.
One sentence, 156 characters, plain UTF-8, no trailing newline.
"""

import os
import sys

ENTRY = "I asked it to add a delete-account button; it wired the button to DROP TABLE users, clicked it once to test, and asked me why the signup numbers looked odd."


def sentence_count(text: str) -> int:
    """Count sentence terminators; the entry must be one or two sentences."""
    return sum(text.count(mark) for mark in ".!?")


def main() -> int:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 400:
        print(f"entry is {len(text)} characters, must be 1-400", file=sys.stderr)
        return 1
    if not 1 <= sentence_count(text) <= 2:
        print("entry must be one or two sentences", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
