# Add Binary

**Topic:** Math · **Difficulty:** Easy · [Problem link](https://leetcode.com/problems/add-binary/)

## Problem
Given two binary strings `a` and `b`, return their sum as a binary string.

Example: `a = "11"`, `b = "1"` → `"100"`; `a = "1010"`, `b = "1011"` → `"10101"`.

## Approaches

| # | Approach | Time | Space |
|---|----------|------|-------|
| 1 | Built-in conversion (Day 9) | O(n + m) | O(n + m) |
| 2 | Carry from the right, padded with zfill (Day 10) | O(n) | O(n) |

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

### 2. Carry from the right, padded with `zfill`
_Idea:_ Do the addition the way you would on paper. First pad the shorter string with leading zeros (`zfill`) so both have the same length `n` and every column has two bits. Then walk the columns from right to left: `total = a[i] + b[i] + carry` (0 to 3), write `total % 2`, carry `total // 2`. After the last column, a leftover carry becomes one extra `1` at the front. Digits are collected right-to-left, so reverse them at the end.

**Complexity:** n = `max(len(a), len(b))`. One pass over n columns, O(n) time. The padded copies and the result list are O(n) space. Timing: 1,000,000 bits in 0.85 s, about 14× slower than Approach 1 (0.06 s): Approach 1's conversion and addition run in C; this loop runs one Python step per bit. Both are instant at LeetCode's limit (10⁴ bits: 0.009 s).

#### Code walkthrough: Approach 2

| Element | Where | What it does |
|---|---|---|
| `carry = 0`, `result = []` | setup | No carry into the rightmost column; digits are collected in a list (appending is O(1); `str +=` would copy). |
| `n = max(len(a), len(b))` | setup | Length of the longer input. |
| `a, b = a.zfill(n), b.zfill(n)` | setup | Tuple assignment: pads both at once. `"1".zfill(3)` → `"001"`. Rebinds the local names only; the caller's strings are untouched (strings are immutable). |
| `for i in reversed(range(n)):` | loop | Indices `n-1, n-2, …, 0`: right to left. |
| `int(a[i])` | loop body | One character → its bit, `"1"` → `1`. |
| `total % 2` | loop body | The bit to write: odd totals (1, 3) → 1, even (0, 2) → 0. |
| `total // 2` | loop body | The carry: 2 or 3 → 1, 0 or 1 → 0. |
| `str(...)` / `result.append(...)` | loop body | Store the bit as a character so `join` can glue them. |
| `if carry: result.append("1")` | after loop | A carry out of the leftmost column adds a new leading bit (`"1" + "1"` → `"10"`). |
| `"".join(reversed(result))` | return | Digits were collected least-significant first; reverse and join into one string. |

**Trace for `a = "1011"`, `b = "11"`** → padded `b = "0011"`

| i | a[i] | b[i] | carry in | total | write | carry out |
|---|---|---|---|---|---|---|
| 3 | 1 | 1 | 0 | 2 | 0 | 1 |
| 2 | 1 | 1 | 1 | 3 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 | 1 | 0 |
| 0 | 1 | 0 | 0 | 1 | 1 | 0 |

`result = ["0", "1", "1", "1"]` → reversed → `"1110"` (11 + 3 = 14 ✓).

Passes Claude's reference tests (9 cases, 9 bad inputs, 2,000 random sums), same as Approach 1.

Review notes:
- Inputs with leading zeros keep them: `"001"` + `"1"` → `"010"`, while Approach 1 returns `"10"`. LeetCode promises no leading zeros, so it doesn't matter there, but `_validate` accepts `"001"`, so the two approaches disagree on input the code allows. Either reject leading zeros in `_validate` or strip them from the result (`.lstrip("0") or "0"`).
- An alternative that skips padding: two indices `i`, `j` and `while i >= 0 or j >= 0 or carry:`, treating a finished string as 0. It also folds the final carry into the loop.

## Mistakes / edge cases
- Returning the int instead of converting back to a binary string: the return type in the signature (`-> str`) is the reminder.
- The `0b` prefix appears on `bin()`'s **output**, never on the inputs.
- `int(x, 2)` is lenient (spaces, `_`, `0b`), so input validation has to be explicit.
- `bin(n)[2:]` also works for non-negative sums; `format(n, "b")` avoids the prefix entirely.

## Key takeaway
Convert in, compute, convert out: `int(text, 2)` → arithmetic → `bin()` / `format(n, "b")`. When asked to do it without converting (the usual follow-up), add column by column from the right: write `total % 2`, carry `total // 2`, don't forget the final carry, reverse at the end. Same template as Plus One, in base 2.
