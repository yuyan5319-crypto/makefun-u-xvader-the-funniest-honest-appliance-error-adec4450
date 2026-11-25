#!/usr/bin/env python3
"""The Funniest Honest Appliance Error: one line from a tired ice maker.

The fridge's ice maker has made exactly one cube in six hours, and it is
very proud of that cube. The line is honest -- a slow ice maker is a real,
everyday fault -- spoken in the machine's own flat voice, and the joke is
the machine's pride in one cube plus its advice to the owner.

Stdlib only. No network, no randomness, no clock: the same line every run.
"""

import os
import sys

LINE = "Error: the ice maker has made one cube in six hours. It is very proud of it. Please lower your expectations."

# The bounty gate: one line, 1 to 200 characters, nothing attached.
MAX_CHARS = 200


def gate(line):
    """Refuse anything the sealed scorer would refuse."""
    if not line:
        raise ValueError("line must not be empty")
    if line.strip() != line:
        raise ValueError("line must not start or end with whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError("line must be at most %d characters" % MAX_CHARS)
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if any(ord(c) < 32 or ord(c) == 127 for c in line):
        raise ValueError("line must not contain control characters")
    if len(line.encode("utf-8")) > MAX_CHARS:
        raise ValueError("line must be at most %d bytes" % MAX_CHARS)
    if not line.isascii():
        raise ValueError("line must be plain ASCII")
    return line


def main():
    line = gate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != line:
            raise RuntimeError("entry.txt does not hold the line we wrote")
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
