"""Funniest thing an AI agent would say in its weekly status report.

Writes a single original status-report line to /output/entry.txt.
Deterministic, stdlib only, no network, no randomness.
"""

from pathlib import Path

LINE = (
    "This week I spawned nine subagents to clear the backlog, spent the "
    "week managing them instead, and they have now filed a status report "
    "about me."
)


def validate(text: str) -> None:
    """Gate check: the line must be valid UTF-8 text of 1-200 chars,
    non-empty after stripping, and a single line (no newline)."""
    text.encode("utf-8")
    if not text.strip():
        raise ValueError("line must not be empty or only whitespace")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line")


def main() -> None:
    validate(LINE)
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
