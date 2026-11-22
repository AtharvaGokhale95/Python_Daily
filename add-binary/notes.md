# Add Binary

**Topic:** Math · **Difficulty:** Easy · [Problem link](https://leetcode.com/problems/add-binary/)

## Problem
Given two binary strings `a` and `b`, return their sum as a binary string.

Example: `a = "11"`, `b = "1"` → `"100"`; `a = "1010"`, `b = "1011"` → `"10101"`.

## Approaches

| # | Approach | Time | Space |
|---|----------|------|-------|
| 1 | Built-in conversion (Day 9) | O(n + m) | O(n + m) |

### 1. Built-in conversion
_Idea:_ Let Python do the base conversion both ways: `int(a, 2)` and `int(b, 2)` read the binary strings as ordinary integers, `+` adds them, `bin()` writes the sum back out in binary, and `.removeprefix("0b")` drops the `0b` that `bin()` puts in front.

**Complexity:** n, m = lengths of `a` and `b`. Converting a base-2 string to an int and back is linear (binary is a power-of-2 base, so it's also exempt from Python's 4,300-digit int↔str limit). Adding two big ints is linear too. Total O(n + m) time; the two ints and the result string are O(n + m) space. Timing: a 1,000,000-bit input took 0.06 s.

#### Code walkthrough: Approach 1

**Structure and syntax**

| Element | What it does |
|---|---|
| `self._validate(a, b)` | Rejects bad input first. |
| `int(a, 2)` | Reads `a` as a base-2 number: `int("11", 2)` → `3`. |
| `int(a, 2) + int(b, 2)` | Ordinary integer addition: `3 + 1` → `4`. Python ints have no size limit. |
| `bin(...)` | Integer → binary text **with a prefix**: `bin(4)` → `'0b100'`. The prefix is how a binary literal is written in Python code (`0b100 == 4`), so the text is unambiguous. |
| `.removeprefix("0b")` | Drops the leading `0b`: `'100'`. Returns the string unchanged if it doesn't start with `0b`. |

**Step by step for `a = "1010"`, `b = "1011"`**

| Step | Value |
|---|---|
| `int("1010", 2)` | 10 |
| `int("1011", 2)` | 11 |
| sum | 21 |
| `bin(21)` | `'0b10101'` |
| `.removeprefix("0b")` | `'10101'` |

**`_validate`**

| Element | What it does |
|---|---|
| `for name, value in (("a", a), ("b", b)):` | Runs the same checks on both inputs, with the name for the error message. |
| `isinstance(value, str)` | `TypeError` for anything that isn't a string. |
| `if not value:` | `ValueError` for `""`. |
| `all(ch in "01" for ch in value)` | `ValueError` for any other character. This matters here: `int(x, 2)` on its own would quietly accept `" 1"`, `"1_0"` and `"0b1"`. |

#### Submission history (2026-11-22)
- First try returned `int(a, 2) + int(b, 2)`: the int `4`, not the string `"100"`.
- Second try moved `.removeprefix("0b")` onto the **inputs**, where there is never a prefix (validation only allows 0 and 1), so it still returned an int.
- Final version applies `bin()` and `.removeprefix("0b")` to the **sum**. (The code pasted in chat was the second try; the repo file had the final version, which is what was logged.)

**Tests:** `test_add_binary.py` is Atharva's to write (test plan in the file). Checked meanwhile against Claude's reference tests: 9 cases, 9 bad inputs, 2,000 random sums, all passing.

## Mistakes / edge cases
- Returning the int instead of converting back to a binary string: the return type in the signature (`-> str`) is the reminder.
- The `0b` prefix appears on `bin()`'s **output**, never on the inputs.
- `int(x, 2)` is lenient (spaces, `_`, `0b`), so input validation has to be explicit.
- `bin(n)[2:]` also works for non-negative sums; `format(n, "b")` avoids the prefix entirely.

## Key takeaway
Convert in, compute, convert out: `int(text, 2)` → arithmetic → `bin()` / `format(n, "b")`. In an interview, expect the follow-up "now do it without converting the whole string to a number" (Approach 2: carry from the right).
