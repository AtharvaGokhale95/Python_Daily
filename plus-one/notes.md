# Plus One

**Topic:** Math · **Difficulty:** Easy · [Problem link](https://leetcode.com/problems/plus-one/)

## Problem
You are given a large integer as a list `digits`, most significant digit first, with no leading `0`s. Add one to the integer and return the resulting list of digits.

Example: `[1, 2, 9]` → `[1, 3, 0]`; `[9, 9]` → `[1, 0, 0]`.

## Approaches

| # | Approach | Time | Space |
|---|----------|------|-------|
| 1 | String conversion (Day 5) | O(n) | O(n) |
| 2 | Using map() (Day 6) | O(n) | O(n) |
| 3 | Carry from the right (in place) (Day 6) | O(n) worst, O(1) typical | O(1) extra (O(n) if all 9s) |

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
_Idea:_ Same plan as Approach 1 (digits → string → int → +1 → string → digits), written in two lines. `map(str, digits)` turns every digit into a one-character string, `"".join(...)` glues them into one string, and `int(...)` parses it. After adding 1, `str(...)` turns the number back into text and `map(int, ...)` turns each character back into a digit; `list(...)` collects them. O(n) time and O(n) space; the same 4,300-digit `int` ↔ `str` limit as Approach 1 applies.

#### Code walkthrough: Approach 2

`_validate`, the docstring, `short()` and the test harness are the same as in Approach 1. New in this approach:

**Structure and syntax**

| Element | Where | What it does |
|---|---|---|
| `map(str, digits)` | line 1 | `map(function, iterable)` applies `str` to every digit. It returns a **lazy iterator**: nothing is computed until something consumes it. |
| `"".join(...)` | line 1 | Consumes the iterator and concatenates the strings with `""` (nothing) between them: `["1", "2", "9"]` → `"129"`. Replaces Approach 1's `+=` loop. |
| `int("...")` | line 1 | Parses the string into a number. |
| `str(integer + 1)` | line 2 | Adds 1, then converts back to text: `130` → `"130"`. |
| `map(int, "130")` | line 2 | A string is iterable one character at a time, so `int` is applied to `"1"`, `"3"`, `"0"`. |
| `list(map(...))` | line 2 | Consumes the lazy iterator into a real list, which is what the method must return. Without `list(...)` you'd return a `map` object. |
| Nested calls | both lines | Read inside-out: `int("".join(map(str, digits)))` runs `map` first, then `join`, then `int`. |

**Trace for `digits = [1, 2, 9]`**

| Step | Value |
|---|---|
| `map(str, digits)` | `"1"`, `"2"`, `"9"` (lazy) |
| `"".join(...)` | `"129"` |
| `int(...)` | `129` |
| `integer + 1` | `130` |
| `str(...)` | `"130"` |
| `list(map(int, ...))` | `[1, 3, 0]` |

**Test cases:** the same 9 cases and 6 bad inputs as Approach 1. All 15 pass. Also checked against a carry-based reference on 20,000 random inputs with no mismatches.


### 3. Carry from the right (in place)
_Idea:_ Do the addition the way you would on paper. Start at the last digit. If it's below 9, add 1 and you're done: return immediately. If it's 9, it becomes 0 and the 1 carries to the digit on its left; repeat. If the loop finishes, every digit was 9 and is now 0, so the answer is `1` followed by all those zeros.

**Complexity:**
- Time: O(n) in the worst case (all 9s), but usually O(1): the loop stops at the first digit below 9, and 9 out of 10 random numbers stop at the very last digit.
- Space: O(1) extra; the digits are changed **in place**. Only the all-9s case builds a new list of n + 1 digits with `[1] + digits`.
- No string conversion, so no 4,300-digit limit: 1,000,000 nines takes about 0.75 s.

**Side effect to mention in an interview:** because it edits `digits` in place, the caller's list changes too (`d = [1, 2, 3]; plusOne(d)` leaves `d == [1, 2, 4]`). In the all-9s case the caller's list becomes all zeros, and a different, new list is returned. Approaches 1 and 2 never touch the input.

#### Code walkthrough: Approach 3

`_validate`, the docstring, `short()` and the test harness are the same as in Approach 1. New in this approach:

**Structure and syntax**

| Element | Where | What it does |
|---|---|---|
| `end = len(digits)` | before the loop | Number of digits. |
| `reversed(range(end))` | loop header | `range(end)` is `0, 1, ..., end-1`; `reversed(...)` walks it backwards: `end-1, ..., 1, 0`. Same as `range(end - 1, -1, -1)`, easier to read. |
| `digits[i] < 9` | `if` | Can this digit absorb the +1 without carrying? |
| `digits[i] += 1` then `return digits` | `if` branch | Adds 1 in place and stops: no further digits change. |
| `else: digits[i] = 0` | `else` branch | A 9 rolls over to 0; the loop moves left, carrying the 1. |
| `return [1] + digits` | after the loop | Reached only if every digit was 9. `+` on two lists builds a **new** list: `[1] + [0, 0, 0]` → `[1, 0, 0, 0]`. |
| Comment block with `eg 1` / `eg 2` / `eg 3` | after the method | Worked examples for no carry, one carry and all 9s. |

**Trace for `digits = [1, 2, 9]`**

| `i` | `digits[i]` | Action | `digits` after |
|---|---|---|---|
| 2 | 9 | `else`: set to 0, carry left | `[1, 2, 0]` |
| 1 | 2 | `< 9`: add 1, return | `[1, 3, 0]` |

**Trace for `digits = [9, 9]`**

| `i` | `digits[i]` | Action | `digits` after |
|---|---|---|---|
| 1 | 9 | set to 0 | `[9, 0]` |
| 0 | 9 | set to 0 | `[0, 0]` |
| loop ends | | `return [1] + digits` | returns `[1, 0, 0]` |

**Test cases:** the same 9 cases and 6 bad inputs as Approach 1. All 15 pass. Also checked against the string method on 20,000 random inputs with no mismatches.


## Revisits
| # | Date | Approach | Result | Notes |
|---|---|---|---|---|
| 1 | 2026-11-25 | String conversion | Needed help | First submission failed every test: `self._validate()` was missing its `digits` argument, `string += digit` added an int to a str (`TypeError`: needs `str(digit)`), and `list.append(digit)` stored one-character strings instead of `int(digit)`. Fixed on the second submission. `list = []` still hides the built-in `list` in this method. |
| 1 | 2026-11-25 | Using map() | Needed help | `int("".join(map(str, digits)))`, then `list(map(int, str(integer + 1)))`. Tests pass first time. |
| 1 | 2026-11-25 | Carry from the right | Needed help | `reversed(range(end))`: below 9 add 1 and return, else write 0; `[1] + digits` when every digit was 9. Tests pass first time; it changes the caller's list (in place, as intended). |

Revisit 1 was submitted on 11-26 and logged on its due date (11-25) at Atharva's request; he marked it "needed help", so the schedule restarts: retry due 12-02. All 45 revisit tests pass (15 per method), and 5,000 random inputs match an `int`-based reference for all three methods (inputs without leading zeros, which the problem promises). Timing for 4,000 nines: carry 1.6 ms, map 2.4 ms, string conversion 3.4 ms; the first two methods stop working at 4,300 digits (Python's int-to-string limit), the carry method does not.

Review notes (revisit 1):
- The `"""Approach …"""` strings come after `self._validate(digits)`, so they aren't docstrings. Fourth revisit in a row with this: put the docstring first, then validate.
- Approach 1 failed because of a missing argument and two type mistakes (int vs str); running the revisit tests before submitting catches all three.

## Mistakes / edge cases
- Approach 1: `list = []` shadows the built-in `list` for the rest of the method. It works here, but calling `list(...)` later in the same method would fail with `TypeError: 'list' object is not callable`. Use a name like `result`.
- Approach 1: building a string with `+=` in a loop is fine for 100 digits; `"".join(str(d) for d in digits)` is the idiomatic version.

## Key takeaway
The carry loop is the real algorithm behind "add 1": walk right to left, stop at the first digit that doesn't overflow. It needs no conversions, has no size limit, and usually finishes after one digit.

`map` + `join` compress the convert-and-loop pattern into one line each, but they only hide the work: the string round-trip is still O(n) and still limited to 4,300 digits.

