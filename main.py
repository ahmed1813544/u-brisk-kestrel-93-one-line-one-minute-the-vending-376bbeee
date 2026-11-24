#!/usr/bin/env python3
"""Write the funniest vending-machine pickup line to /output/entry.txt.

Stdlib only. Deterministic: every run writes the same single line.
"""

import os

LINE = "Hey, gorgeous \u2014 my coil has been spinning for you all day, and I don't even need exact change to drop something sweet."
# 118 characters: inside the gate's 1-200 character window, one line.

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
