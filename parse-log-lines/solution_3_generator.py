"""
Parse Log Lines | Approach 3: Generator
Topic: Strings | Difficulty: Easy
No LeetCode page (data Python problem, roadmap #9).

Each line of an application log looks like this:

    2026-11-24 10:41:07 ERROR [auth] Invalid token for user=42

    <date> <time> <LEVEL> [<service>] <message>

Write parseLogs(lines) that turns a list of such lines into a list of records,
in the same order as the input:

    {"timestamp": "2026-11-24T10:41:07", "level": "ERROR",
     "service": "auth", "message": "Invalid token for user=42"}

A line is VALID when all of these hold (anything else is skipped, not an error):
- Surrounding whitespace, including a trailing newline, is ignored.
- The parts are separated by single spaces.
- date is YYYY-MM-DD and time is HH:MM:SS, and together they are a real
  date and time (2026-02-30 or 25:00:00 are invalid). The record's
  "timestamp" is that moment in ISO format: "2026-11-24T10:41:07".
- LEVEL is one of DEBUG, INFO, WARNING, ERROR, CRITICAL (uppercase).
- service is inside square brackets and is non-empty, with no spaces.
- message is everything after "] ", is non-empty, and may itself contain
  spaces, brackets or colons.
Blank lines are skipped too.

Idea: TODO (write a helper generator that loops over the lines and `yield`s one record per valid line (any parsing method inside); parseLogs returns list(generator). This is how you'd stream a huge log file without holding every record in memory)
Time: O(?) | Space: O(?)
"""
from datetime import datetime


class Solution:
    def parseLogs(self, lines: list[str]) -> list[dict]:
        """Return one record per valid log line, in input order; skip the rest.

        Args:
            lines (list[str]): Raw log lines, e.g. read from a file.

        Raises:
            TypeError: lines is not a list, or an element is not a string.

        Returns:
            A list of dicts with the keys "timestamp", "level", "service",
            "message".
        """
        self._validate(lines)
        # TODO: write your solution here
        raise NotImplementedError

    @staticmethod
    def _validate(lines: list[str]) -> None:
        if not isinstance(lines, list):
            raise TypeError(f"lines must be a list, got {type(lines).__name__}")
        if not all(isinstance(line, str) for line in lines):
            raise TypeError("every element of lines must be a str")
