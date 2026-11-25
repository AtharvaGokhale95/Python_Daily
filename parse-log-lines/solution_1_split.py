"""
Parse Log Lines | Approach 1: Split
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

Idea: Parse one line at a time in _parse_line: strip it, split(" ", 4) into
date, time, level, [service], message (maxsplit=4 keeps the message whole).
Reject the line (return None) if there aren't exactly 5 parts, the level isn't
in LEVELS, the service isn't "[...]" with something inside, or date/time
aren't 10/8 characters; datetime.strptime then rejects moments that aren't
real. Valid lines become a dict; parseLogs keeps the non-None ones.
Time: O(total characters), dominated by strptime (~12-25 µs per line) |
Space: O(output)
"""
from datetime import datetime

LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}                        # created a set for valid values for levels
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
        
        records = []                # empty list to store the record for each line in lines
        for line in lines:
            record = self._parse_line(line)
            if record is not None:
                records.append(record)
        return records
    
    @staticmethod
    def _parse_line(line: str) -> dict | None:
        # this method parses 1 line at a time
        
        # s.strip() - remove whitespace from both ends
        # s.split(sep, maxsplit)  - split on sep, at most maxsplit cuts
        
        # split into date, time, level, service, message - 5 parts
        parts = line.strip().split(" ", 4)                              # for a valid string, parts are separated by a single space
        
        # split() returns an array with 5 parts for each line
        if len(parts) != 5:
            return None
        
        # parts is an array which returns 5 elements for each valid line - unpacking of array can only be done after the len(parts) = 5 is completed
        date, time, level, service_tag, message = parts
        
        # if value of level is not in the set, return None
        if level not in LEVELS:
            return None
        
        # service_tag should be enclosed in square bracket, should not be empty and no white spaces
        # len(service_tag) > 2: two square brackets itself count for 2 chars, so len > 2 ensures that there is at least 1 additional char: non-empty and no white spaces
        # not should cover all 3 conditions
        if not (service_tag.startswith("[") and service_tag.endswith("]") and len(service_tag) > 2):
            return None
        
        
        # date gets: YYYY-MM-DD - 10 characters
        # time gets: HH:MM:SS - 8 characters
        # first check if the lenght of date and time elements are acceptable
        if len(date) != 10 or len(time) != 8:
            return None
        
        # date is YYYY-MM-DD and time is HH:MM:SS, and together they are a real date and time
        # datetime.strptime(date_string, format)
        # strptime() check if the values are real
        try:
            moment = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return None
        
        # return values for ideal cases in a form of a dict
        return{
            "timestamp" : moment.isoformat(),                   # "2026-11-24T10:41:07"
            "level": level,
            "service": service_tag[1:-1],                       # drop the "[" and "]" - first and last char
            "message": message,
        }
        
        
        

    @staticmethod
    def _validate(lines: list[str]) -> None:
        if not isinstance(lines, list):
            raise TypeError(f"lines must be a list, got {type(lines).__name__}")
        if not all(isinstance(line, str) for line in lines):
            raise TypeError("every element of lines must be a str")
