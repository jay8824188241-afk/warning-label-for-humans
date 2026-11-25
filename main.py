#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Prints the single-line safety warning label that should come printed on
every human being. Deterministic, standard library only, no network.
Writes the label to /output/entry.txt when that directory exists,
and always prints it to stdout.
"""

LABEL = (
    "WARNING: This human runs on caffeine, confidence, and unfinished plans. "
    "Do not shake, do not rush, and never ask how the diet is going."
)


def main():
    print(LABEL)
    try:
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LABEL + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
