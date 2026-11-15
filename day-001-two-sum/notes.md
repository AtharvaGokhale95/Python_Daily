# Day 1: Two Sum

**Topic:** Arrays & Hashing · **Difficulty:** Easy · [Problem link](https://leetcode.com/problems/two-sum/)

## Problem
Given a list of integers `nums` and an integer `target`, return the indices of the two numbers that add up to `target`. Each input has exactly one solution, and the same element may not be used twice.

## Approaches

| # | Approach | Time | Space |
|---|----------|------|-------|
| 1 | Brute force (check every pair) | O(n²) | O(1) |
| 2 | Optimized | | |

### 1. Brute force
_Idea:_ Check every pair `(i, j)` with `i < j` and return the first pair whose values add up to `target`. Simple and needs no extra memory, but the nested loops make it O(n²).

Also validates input: raises `TypeError` for a non-list or non-int values and `ValueError` when no pair exists.

#### Code walkthrough: Approach 1

**Structure and definitions**

| Element | Where | What it does |
|---|---|---|
| `class Solution:` | top | Defines a class. LeetCode expects solutions as methods on a class named `Solution`. |
| `def twoSum(self, ...)` | method | `def` defines a function; inside a class it's a method. |
| `self` | first parameter | The instance the method is called on. Lets the method call other methods, like `self._validate(...)`. |
| `nums: list[int]`, `target: int` | parameters | Type hints: document the expected types. Python doesn't enforce them at runtime, which is why `_validate` exists. |
| `-> list[int]` / `-> None` | after `)` | Return type hint. `None` means the function returns nothing useful. |
| `"""..."""` | under `def` | Docstring: a triple-quoted string that documents the function. Shown by `help(Solution.twoSum)`. |
| `Raises:` section | docstring | Documents which exceptions the method can throw and why (Google docstring style). |
| `_validate` | method name | A leading `_` marks it as internal ("private by convention"), not meant to be called from outside. |
| `@staticmethod` | decorator above `_validate` | `@` applies a decorator. `staticmethod` means the method takes no `self`; it only uses its arguments. |
| `:` | end of `class`, `def`, `for`, `if`, `try` lines | Starts an indented block. |
| Indentation | everywhere | Python uses indentation (4 spaces) instead of braces to group code. |

**Built-in functions and operations**

| Element | What it does here |
|---|---|
| `len(nums)` | Number of items in the list, stored in `n`. |
| `range(n - 1)` | Produces `0, 1, ..., n-2`. `i` stops one early because the last element has nothing after it to pair with. |
| `range(i + 1, n)` | Produces `i+1, ..., n-1`. Starting at `i + 1` means `j` is always after `i`, so no index is reused and no pair is checked twice. |
| Nested `for` loops | Check every pair `(i, j)`: this is what makes it O(n²). |
| `nums[i]` | `[]` indexes into the list (0-based). |
| `+`, `==` | Addition and equality comparison. `=` (single) is assignment, `==` (double) compares. |
| `return [i, j]` | Builds a new list literal with `[ ]` and returns it, ending the method early. |
| `isinstance(x, int)` | `True` if `x` is an `int` (or a subclass of `int`, such as `bool`). |
| `all(...)` | `True` only if every item is truthy. Stops at the first `False`. |
| `isinstance(x, int) for x in nums` | Generator expression: produces one `True`/`False` per element, lazily, without building a list. |
| `not` | Logical negation. |
| `type(nums).__name__` | `type()` gets the object's class; `.__name__` is the class name as text, e.g. `"str"`. |
| `f"..."` with `{...}` | f-string: values inside `{ }` are inserted into the text. |
| `{nums!r}` | `!r` inserts `repr(nums)` instead of `str(nums)`, so strings show their quotes: `'123'` rather than `123`. |
| `exc.__name__` | Name of the exception class, e.g. `"ValueError"`. |

**Exception handling**

| Element | What it does here |
|---|---|
| `raise ValueError(...)` | Signals "the input is the right type but has no valid answer" (no pair adds up to target). |
| `raise TypeError(...)` | Signals "the input is the wrong type" (not a list, non-int element, non-int target). |
| `try: ... except exc: pass` | Runs the call; if it raises the expected exception, catch it and do nothing (`pass` is an empty statement). |
| `else:` on `try` | Runs only when **no** exception was raised. Here that means the test failed, so it raises `AssertionError`. |
| `except exc` | Exception classes are ordinary values, so they can be stored in a list and caught through a variable. |
| `assert cond, message` | Raises `AssertionError` with `message` if `cond` is false. Used as a lightweight test. |
| `raise AssertionError(...)` | Explicitly fails the test with a clear message. |

**Test harness**

| Element | What it does here |
|---|---|
| `if __name__ == "__main__":` | `__name__` is `"__main__"` only when the file is run directly (`python solution_1_brute_force.py`), not when it's imported. Tests run only in that case. |
| `s = Solution()` | Creates an instance so the method can be called as `s.twoSum(...)`. |
| `#` | Starts a comment. Used to label each test case. |
| `cases = [(...), ...]` | A list of tuples; each tuple is `(nums, target, expected)`. |
| `for nums, target, expected in cases:` | Tuple unpacking: each tuple's three values are assigned to three names in one step. |

**Test cases**

| Input `nums` | `target` | Expected | What it checks |
|---|---|---|---|
| `[2, 7, 11, 15]` | `9` | `[0, 1]` | Basic case |
| `[3, 2, 4]` | `6` | `[1, 2]` | Can't use index 0 twice (`3 + 3`) |
| `[3, 3]` | `6` | `[0, 1]` | Duplicate values at different indices |
| `[-1, -2, -3, -4, -5]` | `-8` | `[2, 4]` | Negative numbers |
| `[0, 4, 3, 0]` | `0` | `[0, 3]` | Zeros |
| `[1, 2, 3]` | `100` | `ValueError` | No pair adds up to target |
| `[]` | `0` | `ValueError` | Empty list (loops never run) |
| `"123"` | `3` | `TypeError` | `nums` is not a list |
| `[1, "2"]` | `3` | `TypeError` | A non-int element |

### 2. Optimized
_Idea:_

## Mistakes / edge cases
- Tested: basic case, can't reuse the same index, duplicates, negatives, zeros, no solution, empty list, wrong types.
- `bool` is a subclass of `int` in Python, so `[True, 1]` passes validation.

## Key takeaway
