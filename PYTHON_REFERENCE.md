# Python Reference

A running list of the Python keywords, built-ins and syntax used in this repo. Each entry has its syntax, what it's for, an example, and the problem where it first appeared. New entries are added as new problems are solved.

## Index

| Category | Entries |
|---|---|
| [Classes and functions](#classes-and-functions) | `class`, `def`, `self`, `@staticmethod`, `_name`, `return` |
| [Type hints and docstrings](#type-hints-and-docstrings) | `x: int`, `-> type`, `list[int]`, `dict[int, int]`, `"""docstring"""`, Args / Raises / Returns |
| [Loops and iteration](#loops-and-iteration) | `for`, `range()`, `enumerate()`, tuple unpacking, generator expression |
| [Built-in functions](#built-in-functions) | `len()`, `isinstance()`, `type()`, `.__name__`, `all()`, `repr()`, `str()`, `print()` |
| [Data structures](#data-structures) | list `[]`, indexing `[i]`, slicing `[::-1]`, dict `{}`, `key in dict`, `d[key]`, `d[key] = value`, tuple `( )` |
| [Operators and expressions](#operators-and-expressions) | `=` vs `==`, `bool` / comparisons, `None`, `+ -`, `not`, `and` (short-circuit), `A if cond else B` |
| [Strings and f-strings](#strings-and-f-strings) | `f"..."`, `{value}`, `!r`, `:,` format spec, `\n`, `' '` vs `" "` |
| [Numbers](#numbers) | `100_000` digit separator |
| [Errors and exceptions](#errors-and-exceptions) | `raise`, `TypeError`, `ValueError`, `AssertionError`, `NotImplementedError`, `try / except / else`, `except ... as e`, `pass`, `assert` |
| [Script structure](#script-structure) | `#` comments, `if __name__ == "__main__":`, indentation and `:` |

---

## Classes and functions

### `class`
**Syntax:** `class Name:` followed by an indented body
**Usage:** Groups related functions (methods) together. LeetCode expects each solution as a method on a class named `Solution`.
```python
class Solution:
    def twoSum(self, nums, target): ...
```
*First used in:* two-sum

### `def`
**Syntax:** `def name(param1, param2):`
**Usage:** Defines a function. Inside a class it's called a method. Outside a class it's a plain function, like the `short()` helper.
```python
def short(nums) -> str:
    return repr(nums)
```
*First used in:* two-sum

### `self`
**Syntax:** first parameter of a method: `def method(self, ...)`
**Usage:** The object the method was called on. Use it to reach other methods and data on the same object.
```python
self._validate(nums, target)
```
*First used in:* two-sum

### `@staticmethod`
**Syntax:** `@staticmethod` on the line above `def`
**Usage:** A method that doesn't need `self`, because it only works with its own arguments. `@` applies a *decorator*, which changes how the function behaves.
```python
@staticmethod
def _validate(nums, target) -> None:
    ...
```
*First used in:* two-sum

### Leading underscore `_name`
**Syntax:** `_validate`
**Usage:** By convention, marks something as internal, not meant to be used from outside the class. Python doesn't enforce it.
*First used in:* two-sum

### `return`
**Syntax:** `return value`
**Usage:** Ends the function immediately and gives `value` back to the caller. Without `return`, a function returns `None`.
```python
if nums[i] + nums[j] == target:
    return [i, j]
```
*First used in:* two-sum

---

## Type hints and docstrings

### Parameter type hints `name: type`
**Syntax:** `def f(x: int, nums: list[int]):`
**Usage:** Documents the expected type. Python does **not** check it at runtime, which is why `_validate` exists.
*First used in:* two-sum

### Return type hint `-> type`
**Syntax:** `def f(...) -> list[int]:`
**Usage:** Documents what the function returns. `-> None` means it returns nothing useful.
*First used in:* two-sum

### Generic types `list[int]`, `dict[int, int]`
**Syntax:** `list[ItemType]`, `dict[KeyType, ValueType]`
**Usage:** Says what's inside a container. They can also annotate variables:
```python
seen: dict[int, int] = {}   # value -> index
```
*First used in:* two-sum

### Docstring `"""..."""`
**Syntax:** a triple-quoted string as the first line inside a function, class or file
**Usage:** Documentation that tools can read, for example with `help(Solution.twoSum)`. Google style uses these sections:
```python
def twoSum(self, nums: list[int], target: int) -> list[int]:
    """Return [i, j] where nums[i] + nums[j] == target.

    Args:
        nums (list[int]): must be a list of ints.
        target (int): must be an int.

    Raises:
        TypeError: wrong input types.
        ValueError: no pair adds up to target.

    Returns:
        The two indices as a list.
    """
```
- **Args:** each parameter as `name (type): description`
- **Raises:** each exception and when it's raised
- **Returns:** what comes back

*First used in:* two-sum

---

## Loops and iteration

### `for` loop
**Syntax:** `for item in iterable:`
**Usage:** Runs the body once for each item. Loops can be nested: the inner loop runs fully for each step of the outer one.
```python
for i in range(n - 1):
    for j in range(i + 1, n):
        ...
```
*First used in:* two-sum

### `range()`
**Syntax:** `range(stop)`, `range(start, stop)`, `range(start, stop, step)`
**Usage:** Produces integers from `start` (default 0) up to, **but not including**, `stop`.
```python
list(range(4))      # [0, 1, 2, 3]
list(range(2, 5))   # [2, 3, 4]
```
*First used in:* two-sum

### `enumerate()`
**Syntax:** `for index, item in enumerate(iterable, start=0):`
**Usage:** Gives both the position and the value on each step. Cleaner than `for i in range(len(nums))` plus `nums[i]`.
```python
for i, num in enumerate([10, 20]):
    print(i, num)   # 0 10, then 1 20
```
*First used in:* two-sum

### Tuple unpacking
**Syntax:** `a, b, c = (1, 2, 3)`, or in a loop header: `for a, b in pairs:`
**Usage:** Assigns each item of a tuple to its own name in one step.
```python
for nums, target, expected in cases:
    ...
```
*First used in:* two-sum

### Generator expression
**Syntax:** `(expression for item in iterable)`. The parentheses can be dropped when it's the only argument of a function.
**Usage:** Produces values one at a time without building a whole list. Often passed to `all()`, `any()` or `sum()`.
```python
all(isinstance(x, int) for x in nums)
```
*First used in:* two-sum

---

## Built-in functions

### `len()`
**Syntax:** `len(obj)`
**Usage:** Number of items in a list, string, dict, and so on.
```python
len([2, 7, 11])   # 3
```
*First used in:* two-sum

### `isinstance()`
**Syntax:** `isinstance(value, type)` or `isinstance(value, (type1, type2))`
**Usage:** `True` if `value` is of that type **or a subclass of it**. Watch out: `bool` is a subclass of `int`, so `isinstance(True, int)` is `True`.
```python
isinstance(5, int)       # True
isinstance("5", int)     # False
isinstance(True, int)    # True (!)
```
*First used in:* two-sum

### `type()` and `.__name__`
**Syntax:** `type(value).__name__`
**Usage:** `type()` returns the value's class, and `.__name__` gives that class's name as text. Useful in error messages.
```python
type("123").__name__   # 'str'
```
*First used in:* two-sum

### `all()`
**Syntax:** `all(iterable)`
**Usage:** `True` if every item is truthy, and `True` for an empty iterable. It stops at the first `False`.
```python
all(x > 0 for x in [1, 2, 3])   # True
```
*First used in:* two-sum

### `repr()`
**Syntax:** `repr(value)`
**Usage:** The developer-facing text of a value. Strings keep their quotes, so you can tell `'3'` from `3`.
```python
repr("123")   # "'123'"
repr([1, 2])  # '[1, 2]'
```
*First used in:* two-sum

### `str()`
**Syntax:** `str(value)`
**Usage:** Converts a value to its text form. Turning a number into a string lets you work with its digits as characters. Note that the minus sign is kept: `str(-121)` is `'-121'`.
```python
str(121)    # '121'
str(-121)   # '-121'
```
*First used in:* palindrome-number

### `print()`
**Syntax:** `print(value1, value2, ..., sep=" ", end="\n")`
**Usage:** Writes text to the terminal.
```python
print(f"PASS x = {x!r} -> {result}")
```
*First used in:* two-sum

---

## Data structures

### List `[ ]` and indexing
**Syntax:** `[a, b, c]`, `nums[i]` (0-based)
**Usage:** An ordered, changeable sequence. `nums[0]` is the first item, `nums[-1]` the last.
```python
nums = [2, 7, 11]
nums[1]   # 7
```
*First used in:* two-sum

### Slicing `[start:stop:step]`
**Syntax:** `seq[start:stop:step]`. Any part can be left out.
**Usage:** Takes a piece of a list or string. `start` is included, `stop` is not. A step of `-1` walks backwards, so `[::-1]` is a reversed copy.
```python
s = "12345"
s[1:3]    # '23'
s[::2]    # '135'
s[::-1]   # '54321'
```
*First used in:* palindrome-number

### Dict `{ }`
**Syntax:** `{}` (empty), `{key: value, ...}`
**Usage:** Maps keys to values with fast lookup (O(1) on average). Note that `{}` is an empty **dict**; an empty set is `set()`.
```python
seen = {}
seen[7] = 1        # add or overwrite key 7
7 in seen          # True: `in` checks keys
seen[7]            # 1
```
*First used in:* two-sum

### Tuple `( )`
**Syntax:** `(a, b, c)`
**Usage:** An ordered sequence that can't be changed. Good for fixed groups like one test case.
```python
([2, 7, 11, 15], 9, [0, 1])   # (nums, target, expected)
```
*First used in:* two-sum

---

## Operators and expressions

### `=` vs `==`
**Syntax:** `x = 5` (assign), `x == 5` (compare)
**Usage:** A single `=` stores a value; a double `==` asks whether two values are equal and gives `True` or `False`.
*First used in:* two-sum

### `bool`, `True` / `False` and comparisons
**Syntax:** `a == b`, `a != b`, `a < b`, ... ; return hint `-> bool`
**Usage:** A comparison already produces `True` or `False`, so it can be returned directly instead of using `if ... return True else return False`.
```python
def isPalindrome(self, x: int) -> bool:
    x_str = str(x)
    return x_str == x_str[::-1]
```
*First used in:* palindrome-number

### `None`
**Syntax:** `None`
**Usage:** Python's "no value". Functions without a `return` give `None`. Check for it with `is None`, not `== None`.
```python
isinstance(None, int)   # False
```
*First used in:* palindrome-number

### `not`
**Syntax:** `not condition`
**Usage:** Flips `True` and `False`.
```python
if not isinstance(nums, list):
    raise TypeError(...)
```
*First used in:* two-sum

### `and` (short-circuit)
**Syntax:** `a and b`
**Usage:** `True` only if both are true. If `a` is false, `b` is **never evaluated**, which lets a safe check guard a risky one.
```python
isinstance(nums, list) and len(nums) > 10   # len() only runs on a list
```
*First used in:* two-sum

### Conditional expression (ternary)
**Syntax:** `value_if_true if condition else value_if_false`
**Usage:** Chooses between two values in one line.
```python
label = "big" if len(nums) > 10 else "small"
```
*First used in:* two-sum

---

## Strings and f-strings

### f-string
**Syntax:** `f"text {expression} text"`
**Usage:** Inserts the value of each `{ }` into the text. An f-string with no `{ }` works but the `f` does nothing.
```python
target = 9
f"No pair adds up to {target}"   # 'No pair adds up to 9'
```
*First used in:* two-sum

### `!r` conversion
**Syntax:** `f"{value!r}"`
**Usage:** Inserts `repr(value)` instead of `str(value)`, so strings show their quotes. Useful in test output.
```python
x = "121"
f"{x}"     # 121
f"{x!r}"   # '121'
```
*First used in:* two-sum

### Format spec `:`
**Syntax:** `f"{value:spec}"`
**Usage:** Controls how a value is formatted. `,` adds thousands separators; `.2f` gives 2 decimals.
```python
f"{100000:,}"    # '100,000'
f"{3.14159:.2f}" # '3.14'
```
*First used in:* two-sum

### Escape sequence `\n`
**Syntax:** `"\n"` inside a string
**Usage:** A newline character. `\t` is a tab.
```python
print("\nAll tests passed")   # blank line first
```
*First used in:* two-sum

### Single vs double quotes
**Syntax:** `'text'` or `"text"`
**Usage:** They're the same in Python. Pick one style and use the other when the text contains a quote: `"it's"`.
*First used in:* two-sum

---

## Numbers

### Digit separator `_`
**Syntax:** `100_000`
**Usage:** Underscores inside a number are ignored. They only make big numbers easier to read. `100_000 == 100000`.
*First used in:* two-sum

---

## Errors and exceptions

### `raise`
**Syntax:** `raise ExceptionType("message")`
**Usage:** Stops the function and signals an error to the caller.
```python
raise ValueError(f"No two numbers add up to {target}")
```
*First used in:* two-sum

### Common exception types
| Exception | Use it when |
|---|---|
| `TypeError` | The value is the wrong **type** (a string where an int was expected). |
| `ValueError` | The type is right but the **value** doesn't work (no pair adds up to the target). |
| `AssertionError` | An `assert` fails, or a test raises it by hand. |
| `NotImplementedError` | A placeholder for code that hasn't been written yet. |

*First used in:* two-sum

### `try / except / else`
**Syntax:**
```python
try:
    ...          # code that might raise
except SomeError:
    ...          # runs only if SomeError was raised
else:
    ...          # runs only if NO exception was raised
```
**Usage:** Handles errors without crashing. In tests, the `else` branch catches the case where an expected error **didn't** happen.
```python
try:
    result = s.twoSum(nums, target)
except exc as e:
    print(f"PASS -> {exc.__name__}: {e}")
else:
    raise AssertionError(f"FAIL -> returned {result}")
```
Exception classes are ordinary values, so `exc` can be a variable holding `ValueError` or `TypeError`.
*First used in:* two-sum

### `except ... as e`
**Syntax:** `except SomeError as e:`
**Usage:** Binds the caught exception to `e`. `str(e)`, or `{e}` in an f-string, gives its message.
*First used in:* two-sum

### `pass`
**Syntax:** `pass`
**Usage:** A statement that does nothing. Used where Python needs a block but there's nothing to do.
```python
except exc:
    pass
```
*First used in:* two-sum

### `assert`
**Syntax:** `assert condition, "message"`
**Usage:** If `condition` is true, nothing happens. If it's false, Python raises `AssertionError` with the message. A lightweight test.
```python
assert result == expected, f"got {result}, expected {expected}"
```
*First used in:* two-sum

---

## Script structure

### Comments `#`
**Syntax:** `# text`
**Usage:** Everything after `#` on that line is ignored by Python.
*First used in:* two-sum

### `if __name__ == "__main__":`
**Syntax:** at the bottom of a file, followed by an indented block
**Usage:** `__name__` is `"__main__"` only when the file is run directly (`python file.py`), not when it's imported. Tests go here so they don't run on import.
*First used in:* two-sum

### Indentation and `:`
**Syntax:** a line ending in `:` starts a block; the block is indented (4 spaces)
**Usage:** Python uses indentation instead of braces to group code under `class`, `def`, `for`, `if`, `try` and so on.
*First used in:* two-sum
