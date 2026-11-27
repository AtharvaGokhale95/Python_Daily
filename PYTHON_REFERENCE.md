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

**`reversed(seq)`**: walks a sequence backwards lazily, without copying it. `reversed(range(n))` gives `n-1, ..., 0` (same as `range(n - 1, -1, -1)`).

**`str.startswith(prefix)` / `str.endswith(suffix)`**: `True` if the string begins/ends with it. Accepts a tuple to test several at once: `name.endswith((".py", ".md"))`. Every string starts with `""`.

**`str.find(sub)` / `str.index(sub)`**: index of the first occurrence of `sub`. When it's missing, `find()` returns `-1` but `index()` raises `ValueError`. Both take optional `start, end`; `rfind()` / `rindex()` search from the right. To just test presence, use `sub in s`.
```python
"sadbutsad".find("sad")   # 0
"leetcode".find("leeto")  # -1
"leetcode".index("leeto") # ValueError: substring not found
```

**`min(items, key=len)` / `max(..., key=...)`**: `key` picks what to compare by and returns the original item: `min(["flow", "fl", "flower"], key=len)` → `'fl'`.

**`map(function, iterable)`**: applies the function to every item and returns a **lazy iterator**; wrap it in `list(...)` to get a list. It can only be consumed once.
```python
list(map(int, "130"))          # [1, 3, 0]
"".join(map(str, [1, 2, 9]))   # '129'
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

**Truthiness**: empty containers (`[]`, `""`, `{}`, `set()`), `0` and `None` are falsy, so `if not strs:` means "if `strs` is empty". Use `is None` when you only mean `None`.

**Short-circuit `and` / `or`**: the right side isn't evaluated if the left side already decides the result.
```python
isinstance(nums, list) and len(nums) > 10   # len() only runs on a list
```

**Chained comparison `a <= x <= b`**: means `a <= x and x <= b`, with `x` evaluated once.
```python
all(0 <= d <= 9 for d in digits)
```

**`==` vs `is`**: `==` asks "are the values equal?"; `is` asks "is it the very same object?". Compare values with `==`; keep `is` for `None`, `True` and `False` (`if x is None`).
Gotcha: equal ints are not always the same object: only small ints (-5 to 256) are shared, so `int("1000") is int("1000")` is `False` while `==` is `True`.

**Return a comparison directly**: a comparison is already `True` or `False`.
```python
return s == s[::-1]
```

**Floor division `//` and modulo `%`**: `n % 10` is the last digit and `n // 10` drops it, so you can take a number apart digit by digit without a string. Build a reversed number with `rev = rev * 10 + digit`.
Gotcha: `//` rounds **down**, not toward zero, so with negatives `-7 // 2 == -4` and `-7 % 10 == 3`. Handle negatives first. `divmod(n, 10)` returns both at once: `(n // 10, n % 10)`.
```python
1234 % 10    # 4
1234 // 10   # 123
```

## Sequences and dicts

**Lists are passed by reference**: a function gets the same list object, so `nums[i] = x` inside it changes the caller's list. That's how "in place" works. Reassigning the name (`nums = [...]`) does not affect the caller.
Copy first if you need the original: `list(nums)`, `nums[:]` or `nums.copy()` (all shallow copies).

**List `+` and `*`**: `[1] + digits` builds a **new** list (O(n)); `[0] * 3` gives `[0, 0, 0]`.
Gotcha: `[[]] * 3` repeats the **same** inner list three times, so changing one changes all; use `[[] for _ in range(3)]`.

**Slicing `seq[start:stop:step]`**: `stop` is excluded. `[::-1]` returns a reversed copy.
```python
"12345"[1:3]   # '23'
"12345"[::-1]  # '54321'
```

**Every pair `i < j` with two loops**: the inner loop starts one past the outer index, so each pair is visited once and no element meets itself. n items give n(n - 1) / 2 pairs, which is O(n^2). A `return` inside the inner loop leaves **both** loops and the function.
```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            return True
return False                       # after both loops: no pair matched
```
`itertools.combinations(nums, 2)` yields the same pairs without index bookkeeping: `any(a == b for a, b in combinations(nums, 2))`.

**`sorted(iterable)` vs `list.sort()`**: `sorted(nums)` returns a **new** sorted list and leaves `nums` alone; `nums.sort()` sorts the list in place and returns `None`, so `x = nums.sort()` leaves `x` as `None`. Both take O(n log n) time (Timsort, which is close to O(n) on data that is already sorted). Use `sorted()` when the caller's list must stay unchanged. Both accept `reverse=True` and `key=...`.
```python
sorted([3, 1, 2])          # [1, 2, 3], original untouched
nums = [3, 1, 2]
nums.sort()                # nums is now [1, 2, 3]; the call itself returned None
```

**Compare each item with the one before it**: `for i in range(1, len(seq)):` starts at the second item, so `seq[i - 1]` is always valid; a list of 0 or 1 items makes the range empty and the loop never runs. After sorting, equal values are neighbours, so `seq[i] == seq[i - 1]` finds duplicates. Same idea in one line: `any(a == b for a, b in zip(seq, seq[1:]))`.

**`set()`**: unordered unique values with O(1) average `in`, `.add(x)` and `.discard(x)`. `{}` is an empty dict, so an empty set must be `set()`.
Order-preserving dedupe in one line: `list(dict.fromkeys(nums))` (dicts keep insertion order).

**`key in dict`**: checks keys, in O(1) time on average, which is why a dict turns an O(n²) search into O(n).
Gotcha: `x in list` is **O(n)**, because it scans the list. Inside a loop that makes the whole thing O(n²); use a `set` or `dict` when you only need membership. Use `not in` for the opposite check.
```python
seen = {}            # {} is an empty dict; an empty set is set()
seen[num] = i        # add or overwrite
if target - num in seen: ...
```

**Variable type hint:** `seen: dict[int, int] = {}` documents keys → values. It isn't enforced at runtime.

**Digit separator:** `100_000 == 100000`.

**Build strings with `"".join(...)`**: `"".join(map(str, [1, 2, 9]))` gives `'129'`. `s += ...` in a loop works but `join` is the idiomatic, guaranteed-linear way.

**`int` ↔ `str` limit**: Python refuses to convert ints with more than 4,300 digits to or from a string (`ValueError: Exceeds the limit (4300)...`). `sys.set_int_max_str_digits(0)` removes the limit. Arithmetic itself has no size limit. Bases that are powers of 2 (binary, octal, hex) are exempt.

**`int(text, base)`**: reads text in another base: `int("100", 2)` → `4`, `int("ff", 16)` → `255`. Lenient: it also accepts spaces around the digits, `_` between them and a matching prefix (`int(" 1_0 ", 2)` → `2`, `int("0b100", 2)` → `4`), so validate first if those should be errors. Base `0` reads the base from the prefix: `int("0x1f", 0)` → `31`.

**`bin(n)` / `oct(n)` / `hex(n)`**: number → text **with a base prefix**, the way you'd write it in code: `bin(4)` → `'0b100'`, `hex(255)` → `'0xff'`. Without the prefix: `format(4, "b")` or `f"{4:b}"` → `'100'` (`"#b"` adds it back). Slicing `bin(n)[2:]` breaks for negatives (`bin(-4)` is `'-0b100'`).

**`str.split(sep, maxsplit)`**: cuts at most `maxsplit` times, so the last piece keeps the rest of the string, separators included: `"a b c d".split(" ", 2)` → `['a', 'b', 'c d']`. With an explicit `" "`, two spaces in a row give an empty string (`"a  b".split(" ")` → `['a', '', 'b']`); `split()` with no argument splits on any run of whitespace and drops empties.

**`str.zfill(width)`**: pads a string with leading `"0"`s up to `width` (keeps a leading sign): `"11".zfill(4)` → `'0011'`. Handy for lining up two numbers digit by digit. Same as `s.rjust(width, "0")` for unsigned strings.

**`str.removeprefix(p)` / `str.removesuffix(s)`** (3.9+): removes `p` from the start only if it's there, otherwise returns the string unchanged: `"0b100".removeprefix("0b")` → `'100'`. Unlike `lstrip("0b")`, which strips any mix of those *characters* (`"0b0011".lstrip("0b")` → `'11'`).

**Don't shadow built-ins**: `list = []`, `str = ...`, `sum = 0` hide the real `list()`, `str()`, `sum()` in that scope; a later `list(x)` then fails with `'list' object is not callable`.

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

**pytest: `parametrize`, `pytest.param`, `pytest.raises`**: one test function runs once per row of data. Stacking two `parametrize` decorators runs every combination. `pytest.param(value, expected, id="name")` gives a row a readable name; `ids=repr` names rows from the value itself. `pytest.raises(Error)` passes only if the code inside the `with` block raises that error.
```python
@pytest.mark.parametrize("nums, expected", [
    pytest.param([1, 2, 1], True, id="duplicate"),
    pytest.param([], False, id="empty"),
])
def test_cases(nums, expected):
    assert solve(nums) is expected      # `is` needs a real bool; `1 == True` would pass `==`

def test_bad_input():
    with pytest.raises(TypeError):
        solve("123")
```

## Dates

**`datetime.strptime(text, format)`**: text → `datetime`; raises `ValueError` if the text doesn't match or isn't a real moment (`2026-02-30`, `25:00:00`). Codes: `%Y` year, `%m` month, `%d` day, `%H` hour (24h), `%M` minute, `%S` second. Lenient: `%m`/`%d`/`%H` also accept ONE digit (`"2026-1-5"` passes), so check lengths/shape first. Slow (~10–25 µs a call).
```python
from datetime import datetime
datetime.strptime("2026-11-24 10:41:07", "%Y-%m-%d %H:%M:%S")
```

**`dt.isoformat()` / `datetime.fromisoformat(text)`**: `datetime` ↔ ISO text `"2026-11-24T10:41:07"`. `fromisoformat` is ~50× faster than `strptime` when the text is already ISO. `dt.strftime(format)` goes the other way with any format.

## Structure

**Module-level constant**: a name defined at the top of the file, outside the class, in CAPS by convention (`LEVELS = {"DEBUG", ...}`): built once when the file is imported, shared by every call. A **set** makes `level in LEVELS` O(1).

**`-> dict | None`** (3.10+): the function returns a dict or `None`. `X | None` is the modern spelling of `Optional[X]`. Check the result with `if record is not None:` (not `if record:`, which also skips an empty dict).

**Class attribute**: a variable defined in the class body (not in `__init__`) is shared by every instance; read it as `self.NAME` or `ClassName.NAME`. Good for constant lookup tables: `VALUES = {"I": 1, "V": 5}`. Assigning `self.NAME = ...` creates an instance attribute that hides it.

**`@staticmethod`**: a method that doesn't take `self`, because it only uses its arguments, like `_validate`.

**Leading underscore `_validate`**: marks a method as internal by convention. Python doesn't enforce it.

**`if __name__ == "__main__":`**: runs only when the file is executed directly, not when it's imported. Tests go here.

**Docstring sections (Google style):** `Args:` (each parameter as `name (type): description`), `Raises:` (each exception and when), `Returns:` (what comes back).
