"""Write one line about a small good thing that happened today.

The line is a small, true-feeling moment from this morning: a street
vendor who always acts like a stranger quietly slipped an extra fried
banana into my bag and whispered, "for the road, kid." The warmth is
the unasked-for kindness; the surprise is the turn from a vendor who
pretends not to know me to someone who was looking out for me all
along; the concrete details are the 6 a.m. hour, the fried banana,
and the whispered words.

Gate guard: the entry must be UTF-8 text of 1 to 200 characters, a
single line, and not only white space - the same gate the sealed
scorer applies to /output/entry.txt. Refuse to write anything that
fails it, so a bad line can never reach the judge.
"""

from pathlib import Path

ENTRY = (
    "At 6 a.m. the street vendor who always pretends not to know me "
    "slipped an extra fried banana into my bag and whispered, "
    "'for the road, kid.'"
)

MIN_CHARS = 1
MAX_CHARS = 200


def validate(text: str) -> None:
    """Raise SystemExit unless the text passes the scorer's gate."""
    if not isinstance(text, str):
        raise SystemExit("entry is not text")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry is {len(text)} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    text.encode("utf-8")  # raises if the text is not valid UTF-8


def main() -> None:
    validate(ENTRY)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
