# Palindrome Number

**Topic:** Math · **Difficulty:** Easy · [Problem link](https://leetcode.com/problems/palindrome-number/)

## Problem
Given an integer `x`, return `True` if `x` is a palindrome, and `False` otherwise. A palindrome reads the same forwards and backwards: `121` is a palindrome; `-121` and `10` are not.

## Approaches

`d` = number of digits in `x` (about log₁₀ x).

| # | Approach | Time | Space |
|---|----------|------|-------|
| 1 | String reversal (Day 3) | O(d) | O(d) |
| 2 | Two pointers (Day 3) | O(d) | O(d) |
| 3 | Reverse half the number (Day 3) | O(d) | O(1) |

### 1. String reversal
_Idea:_ Turn `x` into a string with `str(x)`, reverse it with the slice `[::-1]`, and compare the two. Building the string and its reversed copy takes O(d) time and O(d) extra space.

Negative numbers need no special case: `str(-121)` is `"-121"`, its reverse is `"121-"`, and the two never match. Numbers ending in `0` (other than `0` itself) fail the same way: `"10"` reversed is `"01"`.

**Not really brute force:** brute force means trying every possibility, and nothing is being tried here. This approach and the "reverse half the number" approach both run in O(d) time. The difference is space (O(d) for the strings vs O(1)) and the LeetCode follow-up, which asks you to solve it without converting to a string.

#### Code walkthrough: Approach 1

**Structure and syntax**

| Element | Where | What it does |
|---|---|---|
| `"""..."""` at the top of the file | module docstring | Documents the file: problem, idea and complexity. |
| `class Solution:` | top | LeetCode expects the method on a class named `Solution`. |
| `def isPalindrome(self, x: int) -> bool:` | method | `x: int` is a type hint for the parameter, `-> bool` for the return value. Python doesn't enforce hints at runtime, which is why `_validate` exists. |
| `self` | first parameter | The instance the method is called on; lets it call `self._validate(x)`. |
| Docstring with `Args:` / `Raises:` / `Returns:` | under `def` | Google-style docstring: documents each parameter, the exceptions it can raise, and what it returns. |
| `self._validate(x)` | first line of the method | Checks the input type before doing any work. |
| `x_str = str(x)` | method body | `=` assigns; stores the text form of `x`. |
| `return x_str == x_str_rev` | method body | `==` compares the two strings and produces `True` or `False`, which is returned directly. No `if` needed. |
| `@staticmethod` | above `_validate` | Decorator: the method takes no `self` and only uses its argument. |
| `_validate` | method name | A leading `_` marks it as internal ("private by convention"). |
| `-> None` | `_validate` | The function returns nothing useful; it either passes silently or raises. |
| `:` and indentation | `class`, `def`, `if`, `for`, `try` lines | `:` opens a block; the 4-space indentation defines what is inside it. |

**Built-in functions and operations**

| Element | What it does here |
|---|---|
| `str(x)` | Converts the int to text: `121` → `"121"`, `-121` → `"-121"`. |
| `x_str[::-1]` | Slice syntax `[start:stop:step]`. Leaving start and stop empty means "the whole string"; step `-1` walks it backwards, producing a reversed copy. |
| `==` on strings | `True` only if both strings have the same characters in the same order. |
| `isinstance(x, int)` | `True` if `x` is an `int` or a subclass of `int`. `bool` is such a subclass, so `True` and `False` pass this check. |
| `not` | Logical negation. |
| `type(x).__name__` | `type()` gets the object's class; `.__name__` is its name as text, e.g. `"str"`, `"NoneType"`. |
| `f"..."` with `{...}` | f-string: the values inside `{ }` are inserted into the text. |
| `{x!r}` | `!r` inserts `repr(x)`, so a string shows its quotes: `'121'` rather than `121`. That makes it clear which inputs were strings. |
| `exc.__name__` | Name of the exception class, e.g. `"TypeError"`. |

**Exception handling**

| Element | What it does here |
|---|---|
| `raise TypeError(...)` | Signals "the input is the wrong type" (a string, a float or `None`). |
| `try: result = s.isPalindrome(x)` | Runs the call and stores what it returns, if it returns. |
| `except exc as e:` | Catches the expected exception class (stored in the variable `exc`) and binds the exception object to `e`. `{e}` prints its message. |
| `else:` on `try` | Runs only when **no** exception was raised. For a bad input that means the test failed, so it raises `AssertionError`. `result` is assigned inside the `try`, so the message shows the value this call actually returned. |
| `assert cond, message` | Raises `AssertionError` with `message` if `cond` is false. |

**Test harness**

| Element | What it does here |
|---|---|
| `if __name__ == "__main__":` | `__name__` is `"__main__"` only when the file is run directly, not when it's imported. Tests run only in that case. |
| `s = Solution()` | Creates an instance so the method can be called as `s.isPalindrome(x)`. |
| `cases = [(x, expected), ...]` | A list of tuples, one per test. |
| `for x, expected in cases:` | Tuple unpacking: each tuple's two values go into two names in one step. |
| `bad_inputs = [(x, exc), ...]` | Each tuple holds an input and the exception class it should raise. Exception classes are ordinary values, so they can go in a list. |
| `print(f"PASS ...")` | Prints each passing case. |
| `print("All tests passed")` | Prints only if every check passed, since any failure stops the script first. |

**Test cases**

| Input `x` | Expected | What it checks |
|---|---|---|
| `121` | `True` | Basic palindrome |
| `-121` | `False` | Negative: `"-121"` reversed is `"121-"` |
| `10` | `False` | Trailing zero: `"10"` reversed is `"01"` |
| `0` | `True` | Zero (single digit) |
| `7` | `True` | Single digit |
| `1221` | `True` | Even number of digits |
| `12321` | `True` | Odd number of digits |
| `123` | `False` | Not a palindrome |
| `1000021` | `False` | Zeros in the middle |
| `2147447412` | `True` | Large palindrome |
| `"121"` | `TypeError` | String, not int |
| `12.1` | `TypeError` | Float, not int |
| `None` | `TypeError` | Missing value |

### 2. Two pointers
_Idea:_ Convert `x` to a string, then put one pointer at each end (`head` at index 0, `tail` at the last index). While they haven't met, compare the two characters: if they differ it's not a palindrome; otherwise move both pointers one step toward the middle. Still O(d) time and O(d) space for the string, but it stops at the first mismatch and doesn't build a reversed copy.

The loop runs at most d/2 times. For an odd number of digits the middle character is never compared, which is fine: it always matches itself.

#### Code walkthrough: Approach 2

Class structure, `_validate`, `str()`, the docstring and the test harness are the same as in Approach 1 (see that walkthrough). New in this approach:

**Structure and syntax**

| Element | Where | What it does |
|---|---|---|
| `if len(x_str) == 1: return True` | before the loop | Early return for single characters. Not needed: with one character `head == tail`, so the loop never runs and the function already returns `True`. |
| `head = 0`, `tail = len(x_str) - 1` | pointer setup | Indices of the first and last characters. `len(...) - 1` because indexing is 0-based. |
| `while head < tail:` | loop | Repeats as long as the condition is true. Stops when the pointers meet (odd length) or cross (even length). |
| `x_str[head] != x_str[tail]` | `if` | `!=` is "not equal". One mismatch is enough to answer `False`. |
| `return False` inside the loop | early exit | Leaves the method immediately at the first mismatch. |
| `head += 1`, `tail -= 1` | end of loop body | Augmented assignment: shorthand for `head = head + 1` and `tail = tail - 1`. Moves both pointers inward. |
| `return True` after the loop | end | Reached only if every compared pair matched. |

**Trace for `x = 1221`** (`x_str = "1221"`)

| Step | `head` | `tail` | `x_str[head]` | `x_str[tail]` | Result |
|---|---|---|---|---|---|
| 1 | 0 | 3 | `'1'` | `'1'` | match, move in |
| 2 | 1 | 2 | `'2'` | `'2'` | match, move in |
| 3 | 2 | 1 | | | `head < tail` is false, loop ends, return `True` |

**Test cases:** the same 10 cases and 3 bad inputs as Approach 1. All pass.


### 3. Reverse half the number
_Idea:_ No string at all. Peel digits off the end of `x` with `% 10` and build them into a new number `reverse` with `reverse * 10 + digit`. Stop once `reverse` has caught up with what's left of `x`: at that point you've reversed half the digits. A palindrome's two halves then match. O(d) time (actually about d/2 steps) and **O(1) space**, because only two integers are stored. This answers LeetCode's follow-up: "Could you solve it without converting the integer to a string?"

**Why the early exits are needed:**
- Negative numbers are never palindromes (`-121` vs `121-`).
- A number ending in `0` (other than `0` itself) would need to start with `0`, which no number does. Without this check, `10` would loop to `x = 1`, `reverse = 0`... then `x = 0`, `reverse = 1`, and `x == reverse // 10` would wrongly return `True`.

**Why `reverse // 10` for odd lengths:** with an odd number of digits, `reverse` ends up holding the middle digit too (`12321` stops at `x = 12`, `reverse = 123`). The middle digit matches itself, so `reverse // 10` drops it before comparing.

#### Code walkthrough: Approach 3

Class structure, `_validate`, the docstring and the test harness are the same as in Approach 1 (see that walkthrough). New in this approach:

**Structure and syntax**

| Element | Where | What it does |
|---|---|---|
| `x % 10` | early exit and loop | `%` is modulo, the remainder after dividing. `% 10` gives the last digit: `1234 % 10 == 4`. |
| `x // 10` | loop | `//` is floor division: divide, then round down. `// 10` drops the last digit: `1234 // 10 == 123`. |
| `(x < 0) or (x % 10 == 0 and x != 0)` | early exit | Combines conditions. `and` binds tighter than `or`; the parentheses make that explicit. |
| `x != 0` | early exit | Keeps `0` itself, which ends in 0 but is a palindrome. |
| `reverse = 0` | before loop | Starts the reversed half as an empty number. |
| `while x > reverse:` | loop | Runs until `reverse` has at least as many digits as what's left of `x`, which is the halfway point. |
| `last_digit = x % 10` | loop body | Takes the last digit of what's left of `x`. |
| `reverse = reverse * 10 + last_digit` | loop body | Shifts `reverse` left one decimal place and appends the digit: `12 * 10 + 3 == 123`. |
| `x = x // 10` | loop body | Removes that digit from `x`. |
| `return x == reverse or x == reverse // 10` | end | `True` if the halves match for an even length, or match after dropping the middle digit for an odd length. Returns the `or` of two comparisons directly. |

**Trace for `x = 12321`**

| Step | `last_digit` | `reverse` | `x` | `x > reverse`? |
|---|---|---|---|---|
| start | | 0 | 12321 | yes |
| 1 | 1 | 1 | 1232 | yes |
| 2 | 2 | 12 | 123 | yes |
| 3 | 3 | 123 | 12 | no, stop |
| return | | `123 // 10 == 12` | 12 | `x == reverse // 10` → `True` |

**Trace for `x = 1221`**

| Step | `last_digit` | `reverse` | `x` | `x > reverse`? |
|---|---|---|---|---|
| start | | 0 | 1221 | yes |
| 1 | 1 | 1 | 122 | yes |
| 2 | 2 | 12 | 12 | no, stop |
| return | | 12 | 12 | `x == reverse` → `True` |

**Test cases:** the same 10 cases and 3 bad inputs as Approach 1. All pass. Also checked against the string method for every number from 0 to 199,999 with no mismatches.


## Mistakes / edge cases
- Approach 3: the trailing-zero check is essential, not just a shortcut. Without it, `10` returns `True` (see the idea above).
- Approach 3 header says `rev` in one comment but the variable is `reverse`. Minor.
- Approach 2: the `len(x_str) == 1` check is redundant, because the `while` condition already handles one-character strings. Harmless, but it can be removed.
- Approach 1, first draft: the `if x_str == x_str_rev: return True` branch was followed by the starter file's `raise NotImplementedError`, so every non-palindrome raised instead of returning `False`. `-121` crashed the script. Fixed by returning the comparison directly: `return x_str == x_str_rev`.
- `bool` is a subclass of `int`, so `isPalindrome(True)` passes `_validate` and returns `False` (`"True"` isn't a palindrome). To reject it: `if isinstance(x, bool) or not isinstance(x, int):`.
- Python ints have no fixed size, so there is no overflow risk with large inputs. In languages with 32-bit ints, reversing the whole number can overflow, which is one reason Approach 3 reverses only half.

## Key takeaway
`% 10` and `// 10` let you take a number apart digit by digit without a string. Reversing only half avoids extra work and, in languages with fixed-size ints, avoids overflow.

Two pointers moving inward from both ends is the standard pattern for any "reads the same both ways" check. It stops at the first mismatch and avoids building a reversed copy.

`[::-1]` reverses any string, so "is it a palindrome?" becomes one comparison. The cost is O(d) extra space for the two strings.
