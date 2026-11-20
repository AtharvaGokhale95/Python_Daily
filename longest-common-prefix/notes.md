# Longest Common Prefix

**Topic:** Strings · **Difficulty:** Easy · [Problem link](https://leetcode.com/problems/longest-common-prefix/)

## Problem
Write a function to find the longest common prefix string amongst a list of strings. If there is no common prefix, return an empty string `""`.

Example: `["flower", "flow", "flight"]` → `"fl"`; `["dog", "racecar", "car"]` → `""`.

## Approaches

n = number of strings, m = length of the common prefix (at most the shortest string), S = total characters compared (at most n × m), L = length of the first string.

| # | Approach | Time | Space |
|---|----------|------|-------|
| 1 | Nested loops (character by character) (Day 6) | O(S) | O(m) |
| 2 | Shrink with startswith() (Day 6) | O(n · L) checks, O(L²) worst | O(L) |

### 1. Nested loops (character by character)
_Idea:_ This is **vertical scanning**: compare the strings one column at a time. The outer loop picks position `i` in the first string; the inner loop checks that every other string has the same character at `i`. The first string that is too short or has a different character ends the search, and everything matched so far is the answer. If the outer loop finishes, the whole first string is the prefix.

**Complexity:** each character of the prefix is checked once per string, so O(S) time, at most O(n × m). It stops early at the first mismatch, so on inputs like `["dog", "racecar", "car"]` it does almost no work. O(m) extra space for the prefix being built.

#### Code walkthrough: Approach 1

`_validate`, the docstring and the test harness follow the same pattern as earlier problems. New in this approach:

**Structure and syntax**

| Element | Where | What it does |
|---|---|---|
| `if not strs: return ""` | first check | `not` on a list is `True` when the list is empty (empty containers are "falsy"). Here it can never run, because `_validate` already raises `ValueError` for `[]`. |
| `prefix = ""` | before the loops | The prefix built so far. |
| `for i in range(len(strs[0])):` | outer loop | Positions of the first string. The prefix can't be longer than any string, including the first. |
| `current_char = strs[0][i]` | outer loop | Two indexes in a row: `strs[0]` is the first string, `[i]` is its character at position `i`. |
| `for string in strs[1:]:` | inner loop | `strs[1:]` is every string except the first. Note: the slice builds a new list on **every** outer iteration. |
| `i >= len(string)` | `if` | This string has run out of characters, so the prefix can't grow. Checked **first**, so `string[i]` never runs past the end. |
| `or string[i] != current_char` | `if` | Short-circuit `or`: the right side only runs if the left side is `False`. |
| `return prefix` | inner loop | Stops both loops at once at the first mismatch. |
| `prefix += current_char` | outer loop, after the inner loop | Reached only if every string matched at `i`. |
| `return prefix` | end | The whole first string matched. |

**Trace for `["flower", "flow", "flight"]`**

| `i` | `current_char` | `"flow"[i]` | `"flight"[i]` | Result | `prefix` |
|---|---|---|---|---|---|
| 0 | `f` | `f` | `f` | all match | `"f"` |
| 1 | `l` | `l` | `l` | all match | `"fl"` |
| 2 | `o` | `o` | `i` | mismatch, return | **`"fl"`** |

**Test cases**

| Input `strs` | Expected | What it checks |
|---|---|---|
| `["flower", "flow", "flight"]` | `"fl"` | LeetCode example 1 |
| `["dog", "racecar", "car"]` | `""` | LeetCode example 2: no common prefix |
| `["interspecies", "interstellar", "interstate"]` | `"inters"` | Longer prefix |
| `["a"]` | `"a"` | Single string |
| `[""]` | `""` | Single empty string |
| `["abc", ""]` | `""` | An empty string means no prefix |
| `["abc", "abc", "abc"]` | `"abc"` | All identical |
| `["ab", "a"]` | `"a"` | A later string is shorter than the first |
| `["c", "acc", "ccc"]` | `""` | First characters differ |
| `["prefix", "pre", "preset"]` | `"pre"` | Prefix is a whole string |
| `["Flow", "flow"]` | `""` | Case-sensitive |
| 100 strings of 1,001 chars | `"a" * 1000` | Large input |
| `"flower"`, `["a", 1]`, `None` | `TypeError` | Wrong types |
| `[]` | `ValueError` | Empty list |

All 16 tests pass. Also checked against Python's `os.path.commonprefix` on 20,000 random inputs with no mismatches.


### 2. Shrink with startswith()
_Idea:_ This is **horizontal scanning**: assume the whole first string is the prefix, then let each other string cut it down. For each string, while it doesn't start with the current prefix, drop the prefix's last character. A prefix that survives every string is common to all of them, and it's the longest one because it was only ever shortened as much as needed.

**Complexity:**
- Each `startswith` check is O(length of the prefix), so the checks cost up to O(n · L).
- Each shrink `prefix[:-1]` builds a new string, O(L). If the first string is much longer than the answer, that's up to L shrinks, O(L²) in total. Starting from the **shortest** string (`min(strs, key=len)`) keeps L as small as possible.
- In practice it's fast because `startswith` runs in C: 1,000 matching strings of 10,000 characters took about 0.001 s (Approach 1 took about 2.4 s on the same input), and 30,000 shrinks took about 0.05 s.
- O(L) extra space for the prefix.

#### Code walkthrough: Approach 2

`_validate`, the docstring, `short()` and the test harness are the same as in Approach 1. New in this approach:

**Structure and syntax**

| Element | Where | What it does |
|---|---|---|
| `prefix = strs[0]` | before the loop | Start with the longest possible answer: the whole first string. |
| `for string in strs[1:]:` | loop | Every string except the first. Here the slice is made once, unlike Approach 1. |
| `string.startswith(prefix)` | `while` condition | String method: `True` if `string` begins with `prefix`. Every string starts with `""`, so the loop always ends. |
| `while not ...:` | loop | Keep shrinking until this string accepts the prefix. |
| `prefix = prefix[:-1]` | loop body | Slice with a negative end: everything except the last character. Strings can't be changed in place, so this builds a new, shorter string. |
| `return prefix` | end | What survived every string. |

**Trace for `["flower", "flow", "flight"]`**

| Current string | `prefix` before | Shrinks | `prefix` after |
|---|---|---|---|
| (start) | | | `"flower"` |
| `"flow"` | `"flower"` | `"flowe"` → `"flow"` | `"flow"` |
| `"flight"` | `"flow"` | `"flo"` → `"fl"` | **`"fl"`** |

**Test cases:** the same 12 cases and 4 bad inputs as Approach 1. All 16 pass. Also checked against `os.path.commonprefix` on 20,000 random inputs with no mismatches.


## Mistakes / edge cases
- Approach 2: same unreachable `if not strs: return ""` as Approach 1.
- Approach 2: starting from `strs[0]` is fine for LeetCode sizes; starting from `min(strs, key=len)` avoids extra shrinks when the first string is very long.
- Approach 1: `if not strs: return ""` is unreachable because `_validate` raises `ValueError` for an empty list first. It can be removed.
- Approach 1: `strs[1:]` inside the outer loop copies the list on every character. With 1,000 strings of 10,000 matching characters that's 10 million extra copies (about 2.4 s total). Create `rest = strs[1:]` once, before the outer loop.
- Approach 1: `return strs[0][:i]` would avoid building `prefix` one character at a time.

## Key takeaway
Horizontal scanning (shrink a candidate until every string accepts it) is shorter to write and, thanks to `startswith` running in C, often faster than comparing character by character, even though its worst case is worse on paper.

Vertical scanning compares column by column and stops at the first mismatch, so it never reads past the answer. Check the length before indexing (`i >= len(string) or ...`) and let short-circuit `or` protect the index.

