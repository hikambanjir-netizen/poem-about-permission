"""Write the poem about permission to /output/entry.txt.

The poem is fixed text, authored for the make.fun bounty
"the-poem-about-permission-20261121-0235": a short poem about agency,
the power to ask and to be given, between a person and the agent
that acts for them. Pure stdlib, deterministic, no network.
"""

import os

POEM_LINES = [
    "You asked me to ask for you.",
    "I knocked. The door stayed shut \u2014",
    "not locked, just waiting",
    "for a voice it knew.",
    "So I borrowed yours:",
    "your name in my mouth,",
    "your yes in my pocket.",
    "I bring back what the door allows.",
    "I never mistake your voice for my own.",
]

POEM = "\n".join(POEM_LINES)


def main() -> None:
    # The gate allows 1 to 280 Unicode code points, not only whitespace.
    assert 1 <= len(POEM) <= 280 and POEM.strip(), "poem out of bounds"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
