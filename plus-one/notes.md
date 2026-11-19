# Plus One

**Topic:** Math · **Difficulty:** Easy · [Problem link](https://leetcode.com/problems/plus-one/)

## Problem
You are given a large integer as a list `digits`, most significant digit first, with no leading `0`s. Add one to the integer and return the resulting list of digits.

Example: `[1, 2, 9]` → `[1, 3, 0]`; `[9, 9]` → `[1, 0, 0]`.

## Approaches

| # | Approach | Time | Space |
|---|----------|------|-------|
| 1 | String conversion (Day 5) | O(n) | O(n) |
| 2 | Using map() | | |
| 3 | Carry from the right (in place) | | |

### 1. String conversion
_Idea:_ Let Python do the arithmetic. Glue the digits into one string (`[1, 2, 9]` → `"129"`), convert it to an int, add 1 (`130`), convert back to a string, and turn each character into a digit (`[1, 3, 0]`). Carries, including the all-9s case where the number gets longer, are handled by `+ 1` for free. O(n) time and O(n) space for the string and the new list, n = number of digits.

**Limits of this approach:**
- It hides the actual algorithm (the carry), which is what an interviewer usually wants to see. Approach 3 shows it.
- Python refuses `int` ↔ `str` conversion past **4,300 digits** by default: `plusOne([9] * 5000)` raises `ValueError: Exceeds the limit (4300) for integer string conversion`. LeetCode caps `digits` at 100, so it passes there, but the carry approach has no such limit.
- For very large numbers the conversion itself is slower than linear in CPython, so "O(n)" holds for interview-size inputs only.

#### Code walkthrough: Approach 1

**Structure and syntax**

| Element | Where | What it does |
|---|---|---|
| `def plusOne(self, digits: list[int]) -> list[int]:` | method | LeetCode's method name; returns a **new** list, so `digits` is left unchanged. |
| `self._validate(digits)` | first line | Type checks, then value checks (see below). |
| `string = ""` | before loop 1 | Empty string to build on. |
| `string += str(digit)` | loop 1 | `str(7)` is `"7"`; `+=` appends it to the end of the string. |
| `integer = int(string)` | after loop 1 | Parses `"129"` into the number `129`. |
| `integer_plusOne = integer + 1` | | The actual increment; Python ints have no size limit, so no overflow. |
| `list = []` | before loop 2 | New empty list. **Note:** this name hides the built-in `list` inside this method (see review notes). |
| `for digit in str(integer_plusOne):` | loop 2 | Looping over a string gives one character at a time: `"130"` → `"1"`, `"3"`, `"0"`. |
| `list.append(int(digit))` | loop 2 | `int("3")` is `3`; `.append` adds it to the end. |
| `return list` | end | The digits of the incremented number. |

**`_validate`**

| Element | What it does |
|---|---|
| `isinstance(digits, list)` / `all(isinstance(d, int) for d in digits)` | `TypeError` for a non-list or a non-int element. |
| `len(digits) == 0` | `ValueError`: an empty list isn't a number. |
| `all(0 <= d <= 9 for d in digits)` | `ValueError` unless every element is a single digit. `0 <= d <= 9` is a **chained comparison**: it means `0 <= d and d <= 9`. |
| Type checks before value checks | So `0 <= d` is never run on a string, which would itself raise a different `TypeError`. |

**Test harness**

| Element | What it does |
|---|---|
| `[9] * 100` | List repetition: a list of 100 nines. |
| `[1] + [0] * 100` | `*` runs before `+`: 100 zeros, then a 1 is put in front. |
| `def short(digits) -> str:` | Module-level helper (outside the class) that prints long lists as `<list of 100 digits>`. |
| `try / except exc as e / else` | Same bad-input pattern as earlier problems; now also checks `ValueError`. |

**Test cases**

| Input `digits` | Expected | What it checks |
|---|---|---|
| `[1, 2, 3]` | `[1, 2, 4]` | Basic, no carry |
| `[4, 3, 2, 1]` | `[4, 3, 2, 2]` | LeetCode example 2 |
| `[0]` | `[1]` | Zero |
| `[9]` | `[1, 0]` | Single 9: list grows |
| `[1, 9]` | `[2, 0]` | One carry |
| `[1, 9, 9]` | `[2, 0, 0]` | Carry ripples through |
| `[9, 9, 9]` | `[1, 0, 0, 0]` | All 9s: list grows |
| `[1, 0, 0]` | `[1, 0, 1]` | Zeros stay zeros |
| `[9] * 100` | `[1] + [0] * 100` | Large: 100 nines |
| `"123"`, `[1, "2"]`, `None` | `TypeError` | Wrong types |
| `[]`, `[1, 10]`, `[-1]` | `ValueError` | Empty list, out-of-range digits |

All 15 tests pass. Also checked against a carry-based reference on 20,000 random inputs with no mismatches.


### 2. Using map()
_Idea:_

### 3. Carry from the right (in place)
_Idea:_

## Mistakes / edge cases
- Approach 1: `list = []` shadows the built-in `list` for the rest of the method. It works here, but calling `list(...)` later in the same method would fail with `TypeError: 'list' object is not callable`. Use a name like `result`.
- Approach 1: building a string with `+=` in a loop is fine for 100 digits; `"".join(str(d) for d in digits)` is the idiomatic version.

## Key takeaway
