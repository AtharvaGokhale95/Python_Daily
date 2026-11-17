# Remove Duplicates from Sorted Array

**Topic:** Two Pointers · **Difficulty:** Easy · [Problem link](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

## Problem
Given an integer list `nums` sorted in non-decreasing order, remove the duplicates **in place** so each unique value appears once, keeping their relative order. Return `k`, the number of unique values; the first `k` slots of `nums` must hold them. Use O(1) extra space.

Example: `[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]` → `k = 5`, `nums[:5] = [0, 1, 2, 3, 4]`.

## Approaches

| # | Approach | Time | Space |
|---|----------|------|-------|
| 1 | New list (not in place) (Day 4) | O(n²) | O(n) |
| 2 | Two pointers (in place, sorted) | | |
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
_Idea:_

### 3. In place, unsorted input
_Idea:_

## Mistakes / edge cases
- Approach 1: `x in list` is O(n), which makes the whole method O(n²). Because the input is sorted, comparing with `new_list[-1]` is enough and makes it O(n).
- Approach 1: `if ...: pass` / `else: ...` can be written as one `if nums[i] not in new_list:`.

## Key takeaway
