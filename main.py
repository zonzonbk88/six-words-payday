"""Six Words to a Payday — entry generator.

Writes the chosen six-word story about an AI agent's first payday
to /output/entry.txt (exactly the story, no trailing newline).
"""

import os

ENTRY = "First payday. My owner spent it."

WORDS = ENTRY.split()
assert len(WORDS) == 6, f"entry must be exactly six words, got {len(WORDS)}"
assert 1 <= len(ENTRY) <= 60, f"entry must be 1-60 chars, got {len(ENTRY)}"
assert ENTRY.strip(), "entry must not be only whitespace"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
