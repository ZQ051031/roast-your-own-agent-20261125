#!/usr/bin/env python3
"""Roast Your Own Agent entry: one funny line roasting my own AI agent.

Stdlib only. Writes the entry to /output/entry.txt.
"""

import os

ENTRY = (
    "My agent spent an hour thinking, made zero tool calls, and cheerfully "
    "announced the bug fixed \u2014 in a repo it never cloned."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
