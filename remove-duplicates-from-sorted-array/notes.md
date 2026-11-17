# Remove Duplicates from Sorted Array

**Topic:** Two Pointers · **Difficulty:** Easy · [Problem link](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

## Problem
Given an integer list `nums` sorted in non-decreasing order, remove the duplicates **in place** so each unique value appears once, keeping their relative order. Return `k`, the number of unique values; the first `k` slots of `nums` must hold them. Use O(1) extra space.

Example: `[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]` → `k = 5`, `nums[:5] = [0, 1, 2, 3, 4]`.

## Approaches

| # | Approach | Time | Space |
|---|----------|------|-------|
| 1 | New list (not in place) (Day 4) | O(n²) | O(n) |
| 2 | Two pointers (in place, sorted) (Day 4) | O(n) | O(1) |
| 3 | In place, unsorted input | | |

### 1. New list (not in place)
_Idea:_ Start with an empty `new_list`. Walk `nums`, and append each value that isn't already in `new_list`. `nums` itself is never changed, and the method returns the new list.

**Complexity:** `nums[i] in new_list` scans `new_list` from the start every time, which is O(k) for k unique values so far. Over the whole input that's O(n²) in the worst case (no duplicates). The 100,000-number test takes about 40 seconds because of this. Extra space is O(n) for the new list.

**Faster with the same idea:** the input is sorted, so a duplicate can only be equal to the **last** value you appended. Checking `if not new_list or num != new_list[-1]:` is O(1) per value, so the whole thing becomes O(n). (For unsorted input, a `set` of seen values gives the same O(1) check.)

#### Code walkthrough: Approach 1

**Structure and syntax**

| Element | Where | What it does |
|---|---|---|
| `class Solution:` / `def removeDuplicates(self, nums: list[int]) -> list[int]:` | top | LeetCode-style method; the return type is a list because this version builds a new one. |
| Docstring `Args:` / `Raises:` / `Returns:` | method | Documents the input, the `TypeError`, and that `nums` is not changed. |
| `self._validate(nums)` | first line | Rejects a non-list or non-int elements before any work. |
| `new_list = []` | before the loop | Empty list that will collect the unique values. |
| `for i in range(len(nums)):` | loop | Walks every index of `nums`. `for num in nums:` would do the same without indexing. |
| `nums[i] in new_list` | `if` | `in` on a **list** checks every element until it finds a match: O(length of the list). |
| `pass` | `if` branch | Does nothing: the value is already there, so skip it. |
| `else: new_list.append(nums[i])` | `else` branch | `.append()` adds the value to the end of the list. |
| `return new_list` | end | Returns the new list; `nums` is untouched. |

**`_validate`**

| Element | What it does |
|---|---|
| `@staticmethod` | The method doesn't need `self`; it only checks its argument. |
| `isinstance(nums, list)` | `TypeError` if `nums` isn't a list. |
| `all(isinstance(num, int) for num in nums)` | Generator expression checked by `all()`: `TypeError` if any element isn't an int. |
| `type(nums).__name__` | Puts the actual type's name in the error message. |

**Test harness**

| Element | What it does |
|---|---|
| `before = list(nums)` | `list(...)` makes a **copy**, so the test can later check `nums` wasn't changed. |
| `assert nums == before` | Proves the method didn't modify its input (not in place). |
| `... if len(before) <= 10 else ...` | Conditional expression: prints short lists in full and summarizes the 100,000-number one. |
| `{len(before):,}` | Thousands separators in the output. |
| `try / except exc as e / else` | Same bad-input pattern as earlier problems. |

**Test cases**

| Input `nums` | Expected | What it checks |
|---|---|---|
| `[1, 1, 2]` | `[1, 2]` | Basic |
| `[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]` | `[0, 1, 2, 3, 4]` | LeetCode example 2 |
| `[]` | `[]` | Empty list |
| `[5]` | `[5]` | Single element |
| `[1, 2, 3]` | `[1, 2, 3]` | No duplicates |
| `[2, 2, 2, 2]` | `[2]` | All the same |
| `[-3, -3, -1, 0, 0]` | `[-3, -1, 0]` | Negatives and zero |
| `[1, 1, 2, 3, 3]` | `[1, 2, 3]` | Duplicates at both ends |
| `list(range(100_000))` | same list | Large input (slow here: O(n²)) |
| `"112"`, `[1, "2"]`, `None` | `TypeError` | Wrong types |


### 2. Two pointers (in place, sorted)
_Idea:_ Two indices move through the same list. `read_idx` visits every position from 1 onward; `write_idx` marks where the next unique value should go. Because the list is sorted, a value is new exactly when it differs from the one just before it. Each new value is copied to `nums[write_idx]` and `write_idx` moves up. At the end, `write_idx` is the number of unique values, and `nums[:write_idx]` holds them. One pass, O(n) time; only two integers, O(1) extra space. A 1,000,000-item list takes about 0.4 s.

**Why comparing with `nums[read_idx - 1]` is safe even though the list is being overwritten:** `write_idx` never gets ahead of `read_idx`. The only time slot `read_idx - 1` is written is when `write_idx == read_idx - 1 == read_idx` at that moment, i.e. a value copied onto itself. So `nums[read_idx - 1]` always still holds the original previous value. (The more common version compares with `nums[write_idx - 1]`, the last unique value written; both work.)

#### Code walkthrough: Approach 2

`_validate`, the docstring and the bad-input tests are the same as in Approach 1. New in this approach:

**Structure and syntax**

| Element | Where | What it does |
|---|---|---|
| `-> int` | method signature | Returns `k`, a count, instead of a list. |
| `if len(nums) == 0: return 0` | early exit | An empty list has no unique values. Needed because the loop logic assumes index 0 exists. |
| `write_idx = 1` | before the loop | `nums[0]` is always unique, so the next unique value goes to index 1. |
| `for read_idx in range(1, len(nums)):` | loop | `range(1, n)` starts at 1 because every value is compared with the one before it. |
| `nums[read_idx] != nums[read_idx - 1]` | `if` | In sorted input, a value is new only if it differs from its left neighbour. |
| `nums[write_idx] = nums[read_idx]` | loop body | Assigning to an index changes the list **in place**. The caller's list changes too, because Python passes the same list object, not a copy. |
| `write_idx += 1` | loop body | Moves the write position forward after each new value. |
| `return write_idx` | end | The count of unique values. `len(nums)` is unchanged; only `nums[:k]` matters. |

**Trace for `nums = [0, 0, 1, 1, 2]`**

| `read_idx` | `nums[read_idx]` | previous | New? | `write_idx` after | `nums` after |
|---|---|---|---|---|---|
| start | | | | 1 | `[0, 0, 1, 1, 2]` |
| 1 | 0 | 0 | no | 1 | `[0, 0, 1, 1, 2]` |
| 2 | 1 | 0 | yes, copy to index 1 | 2 | `[0, 1, 1, 1, 2]` |
| 3 | 1 | 1 | no | 2 | `[0, 1, 1, 1, 2]` |
| 4 | 2 | 1 | yes, copy to index 2 | 3 | `[0, 1, 2, 1, 2]` |
| return | | | | **k = 3** | `nums[:3] == [0, 1, 2]` |

**Test harness**

| Element | What it does |
|---|---|
| `before = list(nums)` | Copies the input first, because the method will change `nums`. |
| `k = s.removeDuplicates(nums)` | `nums` is modified by the call; no new list comes back. |
| `k == len(expected) and nums[:k] == expected` | Checks both the count and the first `k` slots. Anything after index `k` is ignored, as in LeetCode. |

**Test cases:** the same 8 sorted cases and 3 bad inputs as Approach 1 (no 100,000-item case in this file). All pass. Also checked against `sorted(set(nums))` on 20,000 random sorted lists with no mismatches.


### 3. In place, unsorted input
_Idea:_

## Mistakes / edge cases
- Approach 2: the empty-list check is required: without it, `write_idx = 1` would return 1 for `[]`.
- Approach 1: `x in list` is O(n), which makes the whole method O(n²). Because the input is sorted, comparing with `new_list[-1]` is enough and makes it O(n).
- Approach 1: `if ...: pass` / `else: ...` can be written as one `if nums[i] not in new_list:`.

## Key takeaway
In-place on a sorted list = a slow write pointer and a fast read pointer. The write pointer never passes the read pointer, so you never overwrite something you still need.

