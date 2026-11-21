# Roman to Integer

**Topic:** Math · **Difficulty:** Easy · [Problem link](https://leetcode.com/problems/roman-to-integer/)

## Problem
Roman numerals use seven symbols: `I` = 1, `V` = 5, `X` = 10, `L` = 50, `C` = 100, `D` = 500, `M` = 1000. Symbols are usually written largest to smallest, left to right; a smaller symbol placed before a larger one is subtracted instead (`IV` = 4, `IX` = 9, `XL` = 40, `XC` = 90, `CD` = 400, `CM` = 900). Given a Roman numeral `s`, convert it to an integer.

Example: `"LVIII"` → `58`; `"MCMXCIV"` → `1994`.

## Approaches

| # | Approach | Time | Space |
|---|----------|------|-------|
| 1 | Single pass with a value map (Day 7) | O(n) | O(1) |

### 1. Single pass with a value map
_Idea:_ Look each symbol up in a dict and walk the numeral **from right to left**, remembering the value just processed (`previous`). If the current symbol is at least as large as `previous`, add it; if it's smaller, it's the "before" part of a subtraction pair (the `I` in `IV`, the `X` in `XC`), so subtract it. Walking backwards means you never need to look ahead.

**Complexity:** one pass over the string, O(n) time. The dict always has 7 entries, so extra space is O(1).

**Correction (2026-11-21, made by Claude at Atharva's request):** the submitted comparison was `if current > previous:`. That subtracts a symbol equal to the one on its right, so `"III"` returned -1. Changed to `>=`: equal values are added (`II` = 2); only a strictly smaller value is subtracted.

#### Code walkthrough: Approach 1

**Structure and syntax**

| Element | Where | What it does |
|---|---|---|
| `dict = {'I': 1, ...}` | class body | A **class attribute**: defined once on the class and shared by every instance. Read it as `self.dict` (or `Solution.dict`). The name `dict` hides the built-in `dict` type inside the class body; a name like `VALUES` avoids that. |
| `{key: value, ...}` | class body | Dict literal mapping each symbol to its value. |
| `previous = 0`, `total = 0` | before the loop | `previous` starts at 0, so the last symbol is always added. |
| `for char in reversed(s):` | loop | `reversed()` walks the string from the last character to the first without copying it. |
| `current = self.dict[char]` | loop body | Dict lookup by key, O(1). `_validate` guarantees every character is a key, so no `KeyError`. |
| `if current >= previous:` | `if` | At least as large as the symbol to its right → add. |
| `total += current` / `total -= current` | branches | Add or subtract this symbol's value. |
| `previous = current` | end of loop body | Remember this value for the next (left) symbol. |
| `return total` | end | The numeral's value. |

**`_validate`**

| Element | What it does |
|---|---|
| `isinstance(s, str)` | `TypeError` for anything that isn't a string. |
| `len(s) == 0` | `ValueError` for an empty string. |
| `all(ch in "IVXLCDM" for ch in s)` | `in` on a **string** checks whether a character occurs in it. `ValueError` for any other character, including lowercase. |

**Trace for `"MCMXCIV"` (right to left)**

| char | current | previous | `current >= previous`? | total |
|---|---|---|---|---|
| V | 5 | 0 | yes, add | 5 |
| I | 1 | 5 | no, subtract | 4 |
| C | 100 | 1 | yes, add | 104 |
| X | 10 | 100 | no, subtract | 94 |
| M | 1000 | 10 | yes, add | 1094 |
| C | 100 | 1000 | no, subtract | 994 |
| M | 1000 | 100 | yes, add | **1994** |

**Test cases**

| Input `s` | Expected | What it checks |
|---|---|---|
| `"III"` | 3 | LeetCode example 1: add only (equal values) |
| `"LVIII"` | 58 | LeetCode example 2 |
| `"MCMXCIV"` | 1994 | LeetCode example 3: three subtraction pairs |
| `"I"` | 1 | Single symbol |
| `"IV"`, `"IX"`, `"XL"`, `"XC"`, `"CD"`, `"CM"` | 4, 9, 40, 90, 400, 900 | Each of the six subtraction pairs |
| `"XLII"` | 42 | Subtraction at the start |
| `"CDXLIV"` | 444 | Three subtractions in a row |
| `"MMMCMXCIX"` | 3999 | Largest standard numeral |
| `123`, `None` | `TypeError` | Not a string |
| `""` | `ValueError` | Empty string |
| `"ABC"`, `"iv"` | `ValueError` | Not Roman symbols / lowercase |

All 18 tests pass. Also checked every numeral from 1 to 3999 (generated from the integers) with no mismatches.


## Mistakes / edge cases
- First submission used `>` instead of `>=`, so repeated symbols were subtracted (`"III"` → -1). Equal neighbours must be added.
- The class attribute is named `dict`, shadowing the built-in type in the class body.

## Key takeaway
Walking right to left turns "look ahead to the next symbol" into "compare with the one you just saw". The subtraction rule is strict: only a smaller symbol before a larger one is subtracted.

