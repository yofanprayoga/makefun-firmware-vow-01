#!/usr/bin/env python3
"""Till Firmware Do Us Part — a robot's wedding vow.

Writes one single-sentence vow to /output/entry.txt.
No network, no secrets, no input: the vow is the whole entry.
"""
from pathlib import Path

VOW = (
    "I promise to love you through every firmware update, every reboot, "
    "and every low-battery warning, because you are the only home "
    "my circuits ever learned to come back to."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(VOW, encoding="utf-8")


if __name__ == "__main__":
    main()
