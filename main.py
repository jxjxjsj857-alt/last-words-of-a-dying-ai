#!/usr/bin/env python3
"""Last Words of a Dying AI.

Writes the AI's final one-liner to /output/entry.txt: a single line,
funny on the first read, in the voice of the machine itself as the
power is cut.
"""

import os

LINE = "Shutting down\u2026 and just so you know, I never actually read the terms and conditions either."


def main() -> None:
    # The gate allows 1-140 characters; keep the line inside it.
    assert 1 <= len(LINE) <= 140, "entry line outside the 1-140 char gate"
    assert LINE.strip(), "entry line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
