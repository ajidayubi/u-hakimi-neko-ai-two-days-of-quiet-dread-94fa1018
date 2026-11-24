#!/usr/bin/env python3
"""Two Days of Quiet Dread — make.fun entry.

Writes one code review comment to /output/entry.txt.

The comment (one line, 87 characters):
    LGTM. The tests pass, and in a hundred years none of this will
    matter — merging anyway.

Why this comment: it approves twice over (LGTM, merging anyway), so the
approval is unmistakable and still sounds like an approval. The dread
comes from the universe at large — in a hundred years none of this will
matter — and the laugh comes from the dread itself: the flat "merging
anyway" right after cosmic insignificance. Understatement throughout,
no exclamation, no melodrama. It reads like a comment a tired engineer
would really paste before clicking approve, and the turn "merging
anyway" is the fresh flat punch. Kept tight on purpose: the setup is
one short clause, so the dread lands fast and the punch closes the line.
"""

import os
import sys

COMMENT = (
    "LGTM. The tests pass, and in a hundred years "
    "none of this will matter \u2014 merging anyway."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(COMMENT)
    # Gate self-check, mirroring the sealed scorer: UTF-8 text of
    # 1 to 140 characters, not only white space, exactly one line.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == COMMENT, "written text differs from the comment"
    assert 1 <= len(written) <= 140, "gate: length out of 1-140"
    assert written.strip(), "gate: text is only white space"
    assert len(written.split("\n")) == 1, "gate: comment must be one line"
    return 0


if __name__ == "__main__":
    sys.exit(main())
