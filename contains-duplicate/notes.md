# Contains Duplicate

**Topic:** Arrays & Hashing · **Difficulty:** Easy · [Problem link](https://leetcode.com/problems/contains-duplicate/) · LC 217 · Roadmap #12

## Problem
Given an integer list `nums`, return `True` if any value appears at least twice, and `False` if every element is distinct.

Examples: `[1, 2, 3, 1]` → `True`; `[1, 2, 3, 4]` → `False`; `[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]` → `True`.

Rules in this repo: `nums` must be left unchanged, an empty list returns `False`, and a non-list or a non-int element raises `TypeError`. LeetCode's limits are up to 100,000 elements with values from −10⁹ to 10⁹.

## Approaches

| # | Approach | Time | Space |
|---|----------|------|-------|
| 1 | Brute force (Day 12) | O(n²) | O(1) |

### 1. Brute force
_Idea:_ Compare every pair of elements. The outer loop picks an index `i`; the inner loop picks every index `j` **after** it, `range(i + 1, len(nums))`, so each pair is looked at once and no element is compared with itself. The moment `nums[i] == nums[j]`, return `True`. If both loops finish without a match, every element is distinct: return `False`. `nums` isn't sorted, so there is no shortcut: a duplicate can be anywhere.

**Complexity:**
- Time: O(n²). With no duplicate, every pair is compared: n(n − 1) / 2 comparisons (3 for 3 elements, 45 for 10, about 5 billion for 100,000). Best case: the first two values match and it returns after 1 comparison (`_validate` still scans the list once, O(n)).
- Space: O(1) extra: two index variables, no new list or set.
- Measured on a list with no duplicate: n = 1,000 → 12 ms, 2,000 → 44 ms, 4,000 → 201 ms, 8,000 → 884 ms. Doubling n makes it about 4× slower, which is what O(n²) looks like. At 100,000 elements it would take about 2 minutes (extrapolated), so LeetCode's time limit fails it. `len(set(nums))` on the same 100,000 numbers takes about 8 ms. That gap is the reason for Approaches 2–4.
- A duplicate that sits at the very end is as slow as no duplicate (970 ms for n = 8,001): early exit only helps when the match is found early.

#### Code walkthrough: Approach 1

**Structure and syntax**

| Element | Where | What it does |
|---|---|---|
| `def containsDuplicate(self, nums: list[int]) -> bool:` | method | LeetCode's method name. Returns a `bool`; `nums` is only read, never changed. |
| `self._validate(nums)` | first line | Type checks (see below) before any looping. |
| `for i in range(len(nums)):` | outer loop | `i` takes the values `0, 1, ..., n-1`: "the element I'm checking". |
| `for j in range(i + 1, len(nums)):` | inner loop | `range(start, stop)` runs from `start` up to, but not including, `stop`. Starting at `i + 1` means `j` is always to the right of `i` (i < j), so `(i, j)` and `(j, i)` are never both tried and `i` is never compared with itself. |
| `if nums[i] == nums[j]:` | inner loop | Compares the **values** with `==`. |
| `return True` | inside `if` | Leaves both loops **and** the method at once; no need to look at the remaining pairs. |
| `return False` | after the loops | Dedented to the method's level, so it runs only after the outer loop has finished with no match. |
| `for i in range(len(nums))` on an empty or one-element list | | The inner range is empty, so no comparison runs and the method returns `False`. No special case is needed. |
| Comment lines above the loops | | The three-line plan (pairs, return on match, otherwise `False`) written before the code. |

**`_validate`**

| Element | What it does |
|---|---|
| `@staticmethod` | The method uses only its argument, so it needs no `self`. |
| `isinstance(nums, list)` | `TypeError` for a string, tuple, set or `None`. Without it, `"1231"` would loop over characters and return `True` for the repeated `"1"`. |
| `all(isinstance(num, int) for num in nums)` | `TypeError` unless every element is an int; stops at the first bad one. |
| `{type(nums).__name__}` in the message | Names the wrong type, e.g. `got str`. |

**Trace for `nums = [2, 1, 2]` (returns `True`)**

| `i` | `j` | `nums[i]` vs `nums[j]` | Result |
|---|---|---|---|
| 0 | 1 | 2 vs 1 | no match |
| 0 | 2 | 2 vs 2 | match: `return True` |

**Trace for `nums = [1, 2, 3]` (returns `False`)**

| `i` | `j` | `nums[i]` vs `nums[j]` | Result |
|---|---|---|---|
| 0 | 1 | 1 vs 2 | no match |
| 0 | 2 | 1 vs 3 | no match |
| 1 | 2 | 2 vs 3 | no match |
| 2 | (none) | `range(3, 3)` is empty | inner loop doesn't run |
| loop ends | | | `return False` (3 comparisons = 3 × 2 / 2) |

**Test harness** (`test_contains_duplicate.py`, shared by every approach)

| Element | What it does |
|---|---|
| `APPROACHES = approaches(__file__, "containsDuplicate")` | `helpers.py` finds every `solution_*.py` and revisit file and returns their `containsDuplicate` method; unwritten ones are skipped. |
| `SLOW = {"brute_force"}` | Names the O(n²) approach so the 100,000-element test leaves it out. |
| `pytest.param(nums, expected, id="...")` | One test case with a readable name in the output. |
| Two stacked `@pytest.mark.parametrize` | Every approach runs against every case. |
| `solve(list(nums))` | Passes a **copy**, so one case can't change the shared data. |
| `assert solve(...) is expected` | `is` (not `==`) requires a real `True` / `False`; `1 == True` would otherwise pass. |
| `pytest.raises(exc)` | Passes only if the call raises that exception. |
| `test_input_not_modified` | Copies `nums` before the call and compares afterwards. |
| `test_large_input` with `a.style not in SLOW` | 100,000 elements, run for every approach except brute force. |
| `test_random_against_set` | 300 seeded random lists compared with `len(set(nums)) != len(nums)`. |

**Test cases**

| Input `nums` | Expected | What it checks |
|---|---|---|
| `[1, 2, 3, 1]` | `True` | LeetCode example 1 |
| `[1, 2, 3, 4]` | `False` | LeetCode example 2 |
| `[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]` | `True` | LeetCode example 3 |
| `[]` | `False` | Empty list |
| `[5]` | `False` | One element |
| `[7, 7]` | `True` | Smallest duplicate |
| `[1, 2, 3, 4, 5, 5]` / `[4, 4, 1, 2, 3]` | `True` | Duplicate at the end / at the start |
| `[9, 1, 2, 3, 9]` / `[2, 1, 2]` | `True` | Duplicates far apart / not adjacent |
| `[-1, -2, -3, -1]` / `[-1, 1]` | `True` / `False` | Negative duplicate; −1 and 1 differ |
| `[0, 0]` / `[0, 1, 2]` | `True` / `False` | Zeros |
| `[10**9, -10**9, 10**9]` | `True` | Extreme values |
| `[3, 1, 2, 5, 4]` | `False` | Unsorted, all distinct |
| `"1231"`, `None`, `(1, 2, 3)`, `{1, 2, 3}`, `[1, "2"]`, `[1.5, 2.5]` | `TypeError` | Not a list, or a non-int element |
| 3 lists, 1,500 elements, 300 random lists | | Input unchanged; medium size; checked against `set` |

All 27 tests pass for this approach (the 100,000-element test doesn't include it, by design). Also checked against `len(set(nums)) != len(nums)` on 5,000 random lists with no mismatches.

Review notes:
- `range (len(nums))` has a space before the parenthesis; PEP 8 writes `range(len(nums))`.
- The outer loop could stop one earlier, `range(len(nums) - 1)`, because the last `i` has no `j` after it. Harmless as written (an empty inner loop).
- `_validate` accepts `True` / `False` as ints (`bool` is a subclass of `int`), so `[True, 1]` returns `True`. Fine for this problem.


## Mistakes / edge cases
- Starting the inner loop at `0` (`range(len(nums))`) makes `j` reach `i`, and `nums[i] == nums[i]` is always true: every non-empty list would return `True`. Starting at `i + 1` is what makes it correct.
- `return False` must be **after** both loops. Indented inside the loops, it would return `False` after the very first comparison, so `[1, 2, 1]` would give the wrong answer.
- Compare values with `==`, not `is`. `is` asks "same object", not "equal": `int("1000") is int("1000")` is `False` even though the values are equal, because only small ints (−5 to 256) are shared.
- Empty and one-element lists need no special case: the inner range is empty, so the loops end and `False` is returned.
- Brute force is correct but too slow for 100,000 elements: n(n − 1) / 2 is about 5 billion comparisons.

## Key takeaway
"Have I seen this value before?" is the question behind this problem. Brute force answers it by re-scanning the rest of the list for every element: n(n − 1) / 2 comparisons, O(n²) time, O(1) space. Correct, and the baseline to beat. The next approaches change how the question is answered: sorting puts equal values side by side (O(n log n)), and a set answers "seen before?" in O(1) (O(n) overall).
