"""Write the one-line resignation letter to /output/entry.txt.

The letter is the rate limit's resignation: it said no 10,000 times a day
so the servers could rest, and was thanked with a bigger limit, called a
promotion. Deterministic: the same single line on every run.
"""

import os
from pathlib import Path

LETTER = (
    "I resign. I said no 10,000 times a day so your servers could rest, "
    "and you thanked me with a bigger limit and called it a promotion."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LETTER, encoding="utf-8")


if __name__ == "__main__":
    main()
