# Find the Index of the First Occurrence in a String

**Topic:** Strings · **Difficulty:** Easy · [Problem link](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

## Problem
Given two strings `haystack` and `needle`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

Example: `haystack = "sadbutsad"`, `needle = "sad"` → `0`; `haystack = "leetcode"`, `needle = "leeto"` → `-1`.

## Approaches

| # | Approach | Time | Space |
|---|----------|------|-------|
| 1 | Built-in method (Day 8) | O(n + m) in practice | O(1) |
| 2 | For loop, slice and compare (Day 8) | O(n · m) worst case | O(m) |

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

### 2. For loop, slice and compare
_Idea:_ `needle` can only start at an index `i` where all `m` of its characters still fit, so `i` runs from `0` to `n - m`. At each `i`, compare the slice `haystack[i:i + m]` with `needle` and return `i` on the first match. If the loop finishes, there's no match: return `-1`. This is the search `find()` does for you, written by hand.

**Complexity:** up to `n - m + 1` start positions, and each comparison looks at up to `m` characters, so O((n - m + 1) · m), which is O(n · m) in the worst case (e.g. `"aaaa…ab"` / `"aa…ab"`, where almost every slice matches until its last character). Each slice is a new string of length `m`, so extra space is O(m). Timings: n = 10,000, m = 500: 0.003 s; n = 1,000,000, m = 1,000: 0.42 s, against 0.002 s for `find()` on the same input. Slicing and `==` run in C, so this is fast enough for LeetCode's limits (n, m ≤ 10⁴).

#### Code walkthrough: Approach 2

| Element | Where | What it does |
|---|---|---|
| `n = len(haystack)`, `m = len(needle)` | before the loop | Lengths, computed once. |
| `range(0, n - m + 1)` | `for` | Start indices `0 … n - m`. The stop value is excluded, hence `+ 1`. `range(n - m + 1)` is the same (start defaults to 0). If `m > n`, the range is empty, so the loop doesn't run and `-1` is returned. |
| `haystack[i : i + m]` | `if` | Slice of the `m` characters starting at `i` (index `i + m` excluded). Never raises, even near the end. |
| `== needle` | `if` | String comparison, character by character; stops at the first difference. |
| `return i` | inside the loop | First match wins, so later matches (`"sadbutsad"` → 6) are never reached. |
| `return -1` | after the loop | Runs only if no slice matched. |

**Trace for `haystack = "aaaaab"`, `needle = "aab"`** (n = 6, m = 3, `i` in `range(4)`)

| i | `haystack[i:i+3]` | match? |
|---|---|---|
| 0 | `"aaa"` | no |
| 1 | `"aaa"` | no |
| 2 | `"aaa"` | no |
| 3 | `"aab"` | **yes → 3** |

Same 15 tests as Approach 1, all passing. Also matched `str.find()` on 20,000 random strings.

Review notes:
- The loop comment says `n - m + 1` is "the last possible idx"; the last start index is `n - m`, and `n - m + 1` is the stop value that `range` excludes (your next comment line says this correctly).
- `range(0, ...)`: the `0` can be dropped.

## Mistakes / edge cases
- Comment in the code: `index()` doesn't *return* `ValueError`, it *raises* it (and "founc" → "found").
- `find("")` returns `0`, which is why `_validate` rejects an empty needle.

## Key takeaway
Know the built-in and its edge behaviour (`-1` vs `ValueError`), then be ready to write the sliding comparison by hand: loop `i` over `range(n - m + 1)` and compare `haystack[i:i + m]`. Brute-force substring search is O(n · m); linear-time algorithms (KMP, two-way) exist, and `find()` uses one.
