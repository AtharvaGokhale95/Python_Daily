# Parse Log Lines

**Topic:** Strings · **Difficulty:** Easy · Data Python problem (no LeetCode page) · Roadmap #9 · `DE`

## Problem
Each line of an application log looks like `2026-11-24 10:41:07 ERROR [auth] Invalid token for user=42`, i.e. `<date> <time> <LEVEL> [<service>] <message>`. Write `parseLogs(lines)` that returns one record per valid line, in input order:

```python
{"timestamp": "2026-11-24T10:41:07", "level": "ERROR", "service": "auth", "message": "Invalid token for user=42"}
```

Valid = single spaces between the parts; a real `YYYY-MM-DD HH:MM:SS` moment; LEVEL in DEBUG / INFO / WARNING / ERROR / CRITICAL; a non-empty `[service]` with no spaces; a non-empty message (may contain spaces, brackets, colons). Surrounding whitespace is ignored; blank and malformed lines are skipped. `TypeError` if `lines` isn't a list of strings.

## Approaches

| # | Approach | Time | Space |
|---|----------|------|-------|
| 1 | Split (Day 11) | O(total characters), dominated by `strptime` | O(output) |

### 1. Split
_Idea:_ A helper `_parse_line` handles one line and returns a record or `None`. It strips the line and calls `split(" ", 4)`: at most 4 cuts, so there are at most 5 parts and the message (the 5th) stays whole even though it contains spaces. It then rejects the line on the first failed check: not exactly 5 parts, unknown level, service not wrapped in `[...]` with something inside, date/time not 10/8 characters, or `strptime` raising `ValueError`. `parseLogs` collects the non-`None` results.

**Complexity:** every line is stripped, split and checked once: O(total characters) time; the output list is O(number of valid lines) space. In practice the cost is almost all `datetime.strptime`: ~12–25 µs per call vs ~0.3 µs for the split. 1,000,000 lines took 28.7 s. `datetime.fromisoformat(f"{date}T{time}")` does the same check in ~0.2 µs (≈ 70× faster) once the shape has been checked.

#### Code walkthrough: Approach 1

**Structure and syntax**

| Element | Where | What it does |
|---|---|---|
| `from datetime import datetime` | top | Imports the `datetime` class from the `datetime` module. |
| `LEVELS = {"DEBUG", ...}` | module level | A **set** constant, built once at import; `level in LEVELS` is O(1). |
| `records = []` … `if record is not None: records.append(record)` | `parseLogs` | Keeps only parsed lines. `is not None` (not `if record:`) is the precise check for "not skipped". |
| `@staticmethod def _parse_line(line) -> dict \| None` | helper | One line in, a record or `None` out. Splitting the work into "one line" and "all lines" keeps each piece easy to read and test. |
| `line.strip().split(" ", 4)` | helper | `strip()` drops spaces and `\n`/`\r\n` at both ends; `split(" ", 4)` cuts on single spaces at most 4 times. |
| `if len(parts) != 5: return None` | helper | Too few parts: missing field, missing message, or a blank line (`"".split(" ", 4)` → `['']`). |
| `date, time, level, service_tag, message = parts` | helper | Tuple unpacking; safe only after the length check (otherwise `ValueError: not enough values to unpack`). |
| `level not in LEVELS` | helper | Exact, case-sensitive: `"error"` and `"WARN"` are rejected. |
| `startswith("[") and endswith("]") and len(service_tag) > 2` | helper | Brackets present and at least one character inside. No space check needed: a space inside would have been a split point. |
| `len(date) != 10 or len(time) != 8` | helper | Shape check that `strptime` alone misses: `%m`, `%d`, `%H` accept one digit, so `"2026-1-24"` would otherwise pass. |
| `try: datetime.strptime(...) except ValueError: return None` | helper | Parses the moment; impossible dates/times (Feb 30, 25:00) raise `ValueError`. |
| `moment.isoformat()` | return | `datetime` → `"2026-11-24T10:41:07"`. |
| `service_tag[1:-1]` | return | Slice off the first and last character (the brackets). |

**How each kind of bad line is caught**

| Line (after the date/time) | Caught by |
|---|---|
| `ERROR [auth]` (no message) | 4 parts → `len(parts) != 5` |
| `ERROR [auth]message` | 4 parts |
| double space between fields | empty part shifts everything: level becomes `"10:41:07"` → not in `LEVELS` |
| `error [auth] x`, `WARN [auth] x` | `LEVELS` |
| `ERROR auth x`, `ERROR [] x`, `ERROR [auth x` | bracket / length check |
| `ERROR [my svc] x` | the space splits it: `service_tag = "[my"` → no `]` |
| `2026-1-24 …`, `… 9:41:07 …` | length check (9 / 7 characters) |
| `2026-02-30 …`, `… 25:00:00 …` | `strptime` → `ValueError` |

**Tests:** passes all 37 tests in `test_parse_log_lines.py` (11 valid lines, 19 lines that must be skipped, empty list, mixed list keeps order and leaves the input unchanged, 101,000-line input, 4 bad inputs).

Review notes:
- Brackets inside the service aren't rejected: `[a]b]` → service `"a]b"`, `[[x]]` → `"[x]"`. The spec only says "no spaces", so this passes, but `"[" not in service_tag[1:-1] and "]" not in service_tag[1:-1]` would make it strict.
- Speed: see Complexity; `fromisoformat` after the length checks is the cheap swap if you ever parse millions of lines.

## Mistakes / edge cases
- `strptime` is lenient about digit counts; check the shape (lengths) first.
- Unpack `parts` only after checking `len(parts) == 5`.
- `split(" ", 4)`, not `split()`: the no-argument form would merge double spaces (hiding a malformed line) and break the message apart.

## Key takeaway
Parse one line in a helper that returns a record or `None`, reject early on the first failed check, and let a library (`strptime`) validate what's hard to check by hand, after a cheap shape check that covers its blind spots.
