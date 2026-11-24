#!/usr/bin/env python3
"""One loading-screen tip for tired developers and their agents.

The program produces a single tip, no more than two hundred
characters long, meant to flash by while a build runs. It is aimed
at the moment an AI coding agent starts rewriting the same file
for the third time: instead of letting the loop spin on, the tip
says to halt, shut the laptop, and read the error aloud, because
the fault is usually sitting in the prompt rather than in the
code. It stays concrete, speaks to the developer and the agent
together, and steers clear of the worn-out coffee, deadline and
compile gags. Nothing here touches the network or rolls any dice,
so every run writes the same bytes.
"""

MAX_TIP_CHARS = 200
OUT_PATH = "/output/entry.txt"

ADVICE = "Tip: when your agent rewrites the same file a third time, stop it, close the laptop, and read the error out loud -- the bug was in your prompt, not the code."


def _check_line(line: str) -> None:
    """Make sure the tip fits the loading-screen gate."""
    size = len(line)
    if not 1 <= size <= MAX_TIP_CHARS:
        raise ValueError(f"tip is {size} characters, gate allows 1-200")
    if line != line.strip():
        raise ValueError("tip has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("tip must be one line")


def _save_tip(line: str) -> None:
    """Write the tip with no trailing newline."""
    with open(OUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line)


def run() -> None:
    _check_line(ADVICE)
    _save_tip(ADVICE)


if __name__ == "__main__":
    run()
