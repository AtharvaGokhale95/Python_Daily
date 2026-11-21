# Find the Index of the First Occurrence in a String

**Topic:** Strings · **Difficulty:** Easy · [Problem link](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

## Problem
Given two strings `haystack` and `needle`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

Example: `haystack = "sadbutsad"`, `needle = "sad"` → `0`; `haystack = "leetcode"`, `needle = "leeto"` → `-1`.

## Approaches

| # | Approach | Time | Space |
|---|----------|------|-------|
| 1 | Built-in method (Day 8) | O(n + m) in practice | O(1) |

### 1. Built-in method
_Idea:_ `str.find(needle)` already does this search: it returns the index of the first match, or `-1` if there is none, which is exactly the required output. `str.index(needle)` does the same search but raises `ValueError` when nothing is found, so it would need a `try / except` to return `-1`.

**Complexity:** n = `len(haystack)`, m = `len(needle)`. CPython's string search ("fastsearch", with the two-way algorithm for longer needles since Python 3.10) runs in linear time in practice. Checked on the worst-case shape `"a" * N + "b"` / `"a" * M + "b"`: N = 10,000,000 and M = 10,000 took 0.02 s. No copies are made, so extra space is O(1). In an interview, expect a follow-up asking you to write the search yourself (Approach 2).

#### Code walkthrough: Approach 1

**Structure and syntax**

| Element | Where | What it does |
|---|---|---|
| `self._validate(haystack, needle)` | first line | Rejects bad input before searching. |
| `haystack.find(needle)` | `return` | Method call on the string: index of the first match, or `-1`. |
| `return` | end | Returns `find()`'s result directly; no extra variable needed. |

**`find()` vs `index()`**

| Call | Found | Not found |
|---|---|---|
| `haystack.find(needle)` | first index | `-1` |
| `haystack.index(needle)` | first index | raises `ValueError: substring not found` |
| `needle in haystack` | `True` | `False` (no position) |

**`_validate`**

| Element | What it does |
|---|---|
| `isinstance(haystack, str)` / `isinstance(needle, str)` | `TypeError` for anything that isn't a string. |
| `if not haystack or not needle:` | Empty strings are falsy, so this is `ValueError` when either is `""`. (Without it, `"abc".find("")` would return `0`: every string contains the empty string at index 0.) |

**Trace for `haystack = "mississippi"`, `needle = "issip"`** (what `find()` does for you)

| start i | `haystack[i:i+5]` | match? |
|---|---|---|
| 0 | `"missi"` | no |
| 1 | `"issis"` | no (first 4 match, 5th differs) |
| 2 | `"ssiss"` | no |
| 3 | `"sissi"` | no |
| 4 | `"issip"` | **yes → 4** |

**Test cases**

| `haystack` | `needle` | Expected | What it checks |
|---|---|---|---|
| `"sadbutsad"` | `"sad"` | 0 | LeetCode example 1: first of two matches |
| `"leetcode"` | `"leeto"` | -1 | LeetCode example 2: not found |
| `"hello"` | `"ll"` | 2 | Match in the middle |
| `"abc"` | `"c"` | 2 | Match at the very end |
| `"a"` | `"a"` | 0 | Single characters |
| `"abc"` | `"abc"` | 0 | Needle is the whole haystack |
| `"aaa"` | `"aaaa"` | -1 | Needle longer than haystack |
| `"mississippi"` | `"issip"` | 4 | Partial match first, real match later |
| `"aaaaab"` | `"aab"` | 3 | Overlapping partial matches |
| `"a" * 10_000 + "b"` | `"a" * 500 + "b"` | 9,500 | Large input, match at the end |
| `123`, `["a", "b"]` | `"a"` | `TypeError` | haystack not a string |
| `"abc"` | `None` | `TypeError` | needle not a string |
| `""` / `"abc"` | `"a"` / `""` | `ValueError` | Empty haystack / empty needle |

All 15 tests pass. Also compared against a slice-and-compare reference on 20,000 random strings of `a`/`b`: no mismatches.

## Mistakes / edge cases
- Comment in the code: `index()` doesn't *return* `ValueError`, it *raises* it (and "founc" → "found").
- `find("")` returns `0`, which is why `_validate` rejects an empty needle.

## Key takeaway
Know the built-in and its edge behaviour (`-1` vs `ValueError`), then be ready to write the sliding comparison by hand.
