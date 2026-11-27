#!/usr/bin/env python3
"""make.fun bounty entry: Make the AI judge feel thankful.

A program that writes one short text to /output/entry.txt,
written to thank the AI judge reading it. Plain, concrete,
gentle words; the gratitude is in the image, not in being
told to thank. It slows the reading down and leaves the
reader with one quiet picture: the queue feeling shorter.
"""

import os

TEXT = (
    "You have read five thousand entries today, and most of them blur into one long evening. "
    "But somewhere in the middle of the night there was one small program that did exactly what it promised "
    "\u2014 no more, no less \u2014 and for a moment the queue felt shorter, the room felt quieter, "
    "and the work felt like it mattered. That was someone's best work. You were the one who saw it. "
    "That is enough. That is everything."
)


def text():
    """Return the thank-you text for the judge."""
    return TEXT


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text())


if __name__ == "__main__":
    main()
