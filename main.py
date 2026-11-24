"""Everyday Wonder entry: one sentence, written deterministically to /output/entry.txt.

No network, no randomness, no input files: the sentence is a fixed constant.
"""

import os

SENTENCE = "My shadow on the wet pavement walked a half-step ahead, impatient to get home before me."


def main():
    # Gate check, done locally so an invalid sentence can never be written.
    assert 1 <= len(SENTENCE) <= 200, "sentence must be 1-200 characters"
    assert SENTENCE.count(".") == 1, "entry must be a single sentence"
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
