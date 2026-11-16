# Python Cheat Sheet

The less-common Python used in this repo, for quick review before interviews. New items are added as new problems are solved.

## Built-ins

**`all(iterable)`**: `True` if every item is truthy (and `True` for an empty iterable). Stops at the first `False`. `any()` is the opposite: `True` if at least one item is truthy.
```python
all(isinstance(x, int) for x in nums)
```

**`isinstance(value, type)`**: `True` if `value` is that type or a subclass. Accepts a tuple of types: `isinstance(x, (int, float))`.
Gotcha: `bool` is a subclass of `int`, so `isinstance(True, int)` is `True`. Use `isinstance(x, int) and not isinstance(x, bool)` to reject it.

**`type(value).__name__`**: the type's name as text, handy in error messages.
```python
type("123").__name__   # 'str'
```

**`repr(value)`**: developer-facing text; strings keep their quotes.
```python
repr("3")   # "'3'"
str("3")    # '3'
```

**`enumerate(iterable, start=0)`**: index and value together.
```python
for i, num in enumerate(nums): ...
```

## f-strings

**`{value!r}`**: inserts `repr(value)` instead of `str(value)`.
```python
f"{x!r}"   # '121' for the string "121", 121 for the int
```

**`{value:spec}`**: format spec. `,` adds thousands separators; `.2f` gives 2 decimals.
```python
f"{100000:,}"     # '100,000'
f"{3.14159:.2f}"  # '3.14'
```

An f-string with no `{ }` works, but the `f` does nothing.

## Expressions

**Generator expression `(expr for x in items)`**: produces values one at a time with no list built. Parentheses can be dropped when it's the only argument.
```python
sum(x * x for x in nums)
```

**Conditional expression `A if cond else B`**: picks one of two values in one line.
```python
label = f"<{len(nums):,} ints>" if len(nums) > 10 else repr(nums)
```

**Short-circuit `and` / `or`**: the right side isn't evaluated if the left side already decides the result.
```python
isinstance(nums, list) and len(nums) > 10   # len() only runs on a list
```

**Return a comparison directly**: a comparison is already `True` or `False`.
```python
return s == s[::-1]
```

## Sequences and dicts

**Slicing `seq[start:stop:step]`**: `stop` is excluded. `[::-1]` returns a reversed copy.
```python
"12345"[1:3]   # '23'
"12345"[::-1]  # '54321'
```

**`key in dict`**: checks keys, in O(1) time on average, which is why a dict turns an O(n²) search into O(n).
```python
seen = {}            # {} is an empty dict; an empty set is set()
seen[num] = i        # add or overwrite
if target - num in seen: ...
```

**Variable type hint:** `seen: dict[int, int] = {}` documents keys → values. It isn't enforced at runtime.

**Digit separator:** `100_000 == 100000`.

## Errors and testing

**`raise`** and which error to use:
| Exception | When |
|---|---|
| `TypeError` | wrong type (a string where an int was expected) |
| `ValueError` | right type, unusable value (no valid answer) |
| `AssertionError` | an `assert` failed, or a test failed by hand |
| `NotImplementedError` | placeholder for unwritten code |

**`assert condition, message`**: does nothing if the condition is true; otherwise raises `AssertionError(message)`.
```python
assert result == expected, f"got {result}, expected {expected}"
```

**`try / except / else`**: `except` runs only if that error was raised; `else` runs only if **no** error was raised.
```python
try:
    result = s.twoSum(nums, target)   # assign inside try
except ValueError as e:               # `as e` binds the error; {e} is its message
    print(f"PASS -> {e}")
else:
    raise AssertionError(f"FAIL -> returned {result}")
```
Exception classes are ordinary values, so `except exc:` works with `exc` holding `ValueError`.

## Structure

**`@staticmethod`**: a method that doesn't take `self`, because it only uses its arguments, like `_validate`.

**Leading underscore `_validate`**: marks a method as internal by convention. Python doesn't enforce it.

**`if __name__ == "__main__":`**: runs only when the file is executed directly, not when it's imported. Tests go here.

**Docstring sections (Google style):** `Args:` (each parameter as `name (type): description`), `Raises:` (each exception and when), `Returns:` (what comes back).
