# Day 1: Two Sum

**Topic:** Arrays & Hashing · **Difficulty:** Easy · [Problem link](https://leetcode.com/problems/two-sum/)

## Problem
Given a list of integers `nums` and an integer `target`, return the indices of the two numbers that add up to `target`. Each input has exactly one solution, and the same element may not be used twice.

## Approaches

| # | Approach | Time | Space |
|---|----------|------|-------|
| 1 | Brute force, check every pair (Day 1) | O(n²) | O(1) |
| 2 | One-pass hash map (Day 2) | O(n) | O(n) |

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

#### Correction (2026-11-16)

Same algorithm (O(n²) time, O(1) space). Changes to the code:

| Change | What it does |
|---|---|
| `target` is validated before the elements of `nums` | A wrong-type `target` is now reported without first scanning the whole list. |
| `# ...` explanatory comments | Notes on `isinstance`, `assert`, `!r` and `try / except / else` written right in the code. |
| `print(f"PASS ... -> {result}")` after each `assert` | Shows every passing case instead of staying silent. |
| `except exc as e:` | `as e` binds the caught exception object to the name `e`. |
| `{e}` inside the f-string | Inserts `str(e)`, which is the exception's message, e.g. `nums must be a list, got str`. |
| `"\nAll tests passed"` | `\n` is an escape sequence for a newline, so a blank line is printed first. |
| `'__main__'` in single quotes | Same as `"__main__"`: Python treats single and double quotes the same. |
| `f"No two numbers add up to target"` | An f-string with no `{ }` placeholders. It works, but the `f` does nothing, and the message no longer includes the target's value. |

Review notes:
- In the `else:` branch, `{result}` refers to the last value from the earlier `cases` loop, not to anything `twoSum` returned for this bad input. If that branch ever ran, the message would show the wrong value. Fix: `result = s.twoSum(nums, target)` inside the `try`.
- `f"Every element of nums must be an int"` also has no placeholders, so the `f` can be dropped.
- PEP 8 style puts a space after the colon in type hints (`nums: list[int]`) and around operators (`n - 1`, `i + 1`).

### 2. One-pass hash map
_Idea:_ For each number, the partner it needs is `target - num`. Keep a dict of numbers already seen → their index. If the partner is already in the dict, the pair is found. Otherwise store the current number and move on. One pass over the list, and each dict lookup is O(1) on average, so O(n) time. The dict can hold up to n entries, so O(n) space.

**Why check before storing:** for `[3, 3]` with target `6`, checking first means index 0 is stored, then index 1 finds `3` already in `seen` and returns `[0, 1]`. For `[3, 2, 4]` with target `6`, it stops `3` from pairing with itself, because `3` isn't in `seen` yet when it is checked.

#### Code walkthrough: Approach 2

Everything in `_validate`, the class structure, docstring, `raise`, `try / except / else`, `assert`, `!r` and `if __name__ == "__main__":` works the same as in Approach 1 (see that walkthrough). New in this approach:

**Structure and syntax**

| Element | Where | What it does |
|---|---|---|
| `seen: dict[int, int] = {}` | before the loop | Creates an empty dict. `dict[int, int]` is a variable annotation: keys are ints (values from `nums`), values are ints (their indices). |
| `{}` | `seen = {}` | Empty dict literal. (An empty set is `set()`, not `{}`.) |
| `# value -> index` | comment | Documents what the dict maps. |
| `for i, num in enumerate(nums):` | loop | `enumerate` yields `(index, value)` pairs; tuple unpacking puts them into `i` and `num`. Replaces `for i in range(len(nums))` plus `nums[i]`. |
| `complement = target - num` | loop body | `-` subtraction: the value that would complete the pair. |
| `complement in seen` | `if` | `in` on a dict checks the **keys**. Uses hashing, so it's O(1) on average, which is what removes the inner loop. |
| `seen[complement]` | `return` | Looks up the stored index for that key. |
| `return [seen[complement], i]` | loop body | The earlier index comes first, so the result is always `[i, j]` with `i < j`. |
| `seen[num] = i` | loop body | Adds or overwrites the key `num` with its index. |
| `# check BEFORE storing num` | comment | Marks the order that prevents pairing a number with itself. |

**Test harness additions**

| Element | What it does here |
|---|---|
| `100_000` | `_` inside a number is a digit separator for readability. `100_000 == 100000`. |
| `list(range(100_000))` | Builds `[0, 1, ..., 99999]` to test a large input. |
| `label = A if cond else B` | Conditional expression (Python's ternary). Prints `len=100000` instead of the whole list when an assertion fails on a big input. |
| `len(nums) > 10` | Comparison deciding which label to use. |
| `print("All tests passed")` | Prints only if every `assert` and expected exception passed, since any failure stops the script first. |

**Test cases**

| Input `nums` | `target` | Expected | What it checks |
|---|---|---|---|
| `[2, 7, 11, 15]` | `9` | `[0, 1]` | Basic case |
| `[3, 2, 4]` | `6` | `[1, 2]` | Can't use index 0 twice (`3 + 3`) |
| `[3, 3]` | `6` | `[0, 1]` | Duplicate values at different indices |
| `[-1, -2, -3, -4, -5]` | `-8` | `[2, 4]` | Negative numbers |
| `[0, 4, 3, 0]` | `0` | `[0, 3]` | Zeros |
| `[5, 1, 9, 4]` | `13` | `[2, 3]` | Answer at the very end |
| `[-3, 4, 3, 90]` | `0` | `[0, 2]` | Negative + positive |
| `list(range(100_000))` | `199_997` | `[99_998, 99_999]` | Large input; finishes instantly in O(n), would take ~5 billion checks in O(n²) |
| `[1, 2, 3]` | `100` | `ValueError` | No pair adds up to target |
| `[]` | `0` | `ValueError` | Empty list (loop never runs) |
| `[5]` | `10` | `ValueError` | One element can't pair with itself |
| `"123"` | `3` | `TypeError` | `nums` is not a list |
| `[1, "2"]` | `3` | `TypeError` | A non-int element |
| `[1, 2]` | `"3"` | `TypeError` | `target` is not an int |

#### Correction (2026-11-16)

Same algorithm (O(n) time, O(n) space). Changes to the code:

| Change | What it does |
|---|---|
| `Args:` section in the docstring | Documents each parameter as `name (type): description`. |
| `Returns:` section in the docstring | Documents what the method gives back. |
| Comment block above the class | Explains the chain: the docstring's `Raises:` promises the errors, `_validate` raises them, and the `except` tests prove it. |
| Inline `#` comments | Explain `seen`'s keys and values, what `enumerate` yields, and why `num` is stored after the check. |
| `isinstance(num, int) for num in nums` | Same generator expression as before, with `num` as the loop name instead of `x`. |
| `def short(nums) -> str:` | A module-level helper function (outside the class). It formats `nums` for printing. |
| `A if cond else B` in `short` | Conditional expression: returns a summary for long lists, otherwise the full list. |
| `isinstance(nums, list) and len(nums) > 10` | `and` short-circuits: if `nums` isn't a list, `len(nums)` is never evaluated. |
| `{len(nums):,}` | `:` starts a format spec inside the f-string; `,` adds thousands separators, so `100000` prints as `100,000`. |
| `repr(nums)` | Returns the developer-style text of a value, the same thing `!r` does inside an f-string. |
| `print(f"PASS ... {short(nums)} ...")` | Prints each passing case, with long lists shortened. |
| `except exc as e:` and `{e}` | Binds the caught exception to `e` and prints its message. |
| New message `"No two numbers in nums add up to {target}"` | Includes the target's value in the error. |

Review notes:
- In the `else:` branch, `{result}` holds the last value from the `cases` loop (`[99998, 99999]`), not anything from this call. Fix: `result = s.twoSum(nums, target)` inside the `try`.
- The `assert` message uses `{nums}` rather than `{short(nums)}`, so if the large test ever failed it would print all 100,000 numbers.
- `f"Every element in nums must be an int"` has no placeholders, so the `f` can be dropped.
- Typo in the docstring: "intergers" → "integers".

## Mistakes / edge cases
- Tested: basic case, can't reuse the same index, duplicates, negatives, zeros, no solution, empty list, wrong types.
- `bool` is a subclass of `int` in Python, so `[True, 1]` passes validation.

## Key takeaway
Trade space for time: storing what you've already seen in a dict turns a "search the rest of the list" step (O(n)) into a lookup (O(1)), taking the whole solution from O(n²) to O(n).
