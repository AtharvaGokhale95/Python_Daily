# Longest Common Prefix

**Topic:** Strings · **Difficulty:** Easy · [Problem link](https://leetcode.com/problems/longest-common-prefix/)

## Problem
Write a function to find the longest common prefix string amongst a list of strings. If there is no common prefix, return an empty string `""`.

Example: `["flower", "flow", "flight"]` → `"fl"`; `["dog", "racecar", "car"]` → `""`.

## Approaches

n = number of strings, m = length of the common prefix (at most the shortest string), S = total characters compared (at most n × m).

| # | Approach | Time | Space |
|---|----------|------|-------|
| 1 | Nested loops (character by character) (Day 6) | O(S) | O(m) |
| 2 | Shrink with startswith() | | |

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
_Idea:_

## Mistakes / edge cases
- Approach 1: `if not strs: return ""` is unreachable because `_validate` raises `ValueError` for an empty list first. It can be removed.
- Approach 1: `strs[1:]` inside the outer loop copies the list on every character. With 1,000 strings of 10,000 matching characters that's 10 million extra copies (about 2.4 s total). Create `rest = strs[1:]` once, before the outer loop.
- Approach 1: `return strs[0][:i]` would avoid building `prefix` one character at a time.

## Key takeaway
Vertical scanning compares column by column and stops at the first mismatch, so it never reads past the answer. Check the length before indexing (`i >= len(string) or ...`) and let short-circuit `or` protect the index.

