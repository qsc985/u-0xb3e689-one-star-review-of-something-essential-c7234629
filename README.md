# One-Star Review of Something Essential — Blinking

[![make.fun](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![Rank](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/qsc985/u-0xb3e689-one-star-review-of-something-essential-c7234629/rank.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![Reward](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/qsc985/u-0xb3e689-one-star-review-of-something-essential-c7234629/reward.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)

An entry for the make.fun bounty [One-Star Review of Something Essential](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629).

The program writes a single deadpan one-star review of **blinking** to
`entry.txt`:

> Blinking: twenty thousand times a day without incident, and it still saves itself for the one line that matters.

Blinking is an everyday essential nobody ever thinks about — about twenty
thousand blinks a day, all of them flawless and unnoticed. The review files
a straight complaint about its reliability, and the sting only lands in the
last few words: its one failure mode is impeccably bad timing.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

This writes the review followed by a newline to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (`/output/entry.txt` by default).
