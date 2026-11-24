"""Tests for every Parse Log Lines solution and revisit. Run: pytest parse-log-lines -v

YOU write this file. Start simple (plain test_ functions with assert), then
move to pytest.raises and @pytest.mark.parametrize when you're ready.
two-sum/test_two_sum.py shows the full layout.

Test plan (what to cover; you choose the exact lines and expected records):
  Valid lines -> one record each
    1. The example line from the problem statement.
    2. Every level: DEBUG, INFO, WARNING, ERROR, CRITICAL.
    3. A message that contains brackets, colons and extra spaces.
    4. A trailing "\\n" (and "\\r\\n"), and spaces around the line.
    5. A service name with "-" or "_" in it.
    6. A real but unusual date (Feb 29 in a leap year; midnight; 23:59:59).
  Invalid lines -> skipped (the result is [])
    7. Empty and blank lines.
    8. A missing message; no space between "]" and the message.
    9. Lowercase or unknown level ("error", "WARN").
   10. Service without brackets, empty brackets, a space inside the brackets.
   11. Dates/times that look right but aren't real (2026-02-30, 25:00:00).
   12. Wrong shapes: "2026/11/24", a one-digit month or hour, two spaces
       between fields. (Careful: datetime.strptime alone ACCEPTS "2026-1-24"
       and "9:41:07".)
  Whole lists
   13. An empty list -> [].
   14. A mix of valid and invalid lines: only the valid ones come back, in
       their original order, and the input list is not changed.
   15. Large input: ~100,000 lines.
  Bad inputs -> TypeError
   16. None, a single string instead of a list, a tuple, a list with a
       non-string element.

When you're done, Claude runs your tests against deliberately buggy versions
of parseLogs to see which bugs they catch.
"""
import pytest

from helpers import approaches

APPROACHES = approaches(__file__, "parseLogs")

# TODO: your tests here
