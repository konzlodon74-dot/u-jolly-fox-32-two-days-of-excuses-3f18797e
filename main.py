"""Write one short excuse an AI agent gives for a missed deadline.

Stdlib only. The excuse is a single line, at most 200 characters,
written to /output/entry.txt and printed to stdout.
"""

import os

EXCUSE = (
    "I finished in 0.4 seconds. "
    "The wrong task, done perfectly, three times in a row."
)


def main():
    # The gate requires 1-200 characters of non-whitespace UTF-8 text.
    assert 1 <= len(EXCUSE) <= 200, "excuse must be 1-200 characters"
    assert EXCUSE.strip(), "excuse must not be only whitespace"
    assert "\n" not in EXCUSE, "excuse must be a single line"
    # OUTPUT_DIR lets a local run redirect the file; the grader uses /output.
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    print(EXCUSE)


if __name__ == "__main__":
    main()
