"""One-star review of blinking, an everyday essential.

Reasoning: everyone blinks roughly twenty thousand times a day and never
notices, which makes it the perfect deadpan target — a flawless, invisible
service with exactly one failure mode. The grievance is the timing: the
blink always saves itself for the one line you actually need to read.
The review reads as a straight complaint about reliability and only
turns at the end, when the "failure" turns out to be impeccably bad timing.
"""

import os
from pathlib import Path

REVIEW = (
    "Blinking: twenty thousand times a day without incident, "
    "and it still saves itself for the one line that matters."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(REVIEW + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
