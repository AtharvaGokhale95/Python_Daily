# Python_Daily

One Python DSA problem a day. For each problem I write a brute-force solution first, then optimize it step by step, with time and space complexity for every approach.

**Started:** Nov 14, 2026

**Roadmap:** [ROADMAP.md](ROADMAP.md) lists the 92 Python DSA problems (Set 1) I'm working through, grouped by pattern, with my progress.

## Progress

| Day | Date | Problem | Topic | Pattern | Difficulty | Solutions | Folder |
|----:|------|---------|-------|---------|------------|-----------:|--------|
| 1 | 2026-11-14 | [Two Sum](https://leetcode.com/problems/two-sum/): brute force | Arrays & Hashing | Complement lookup in a dict | Easy | 1 | [two-sum](two-sum/) |
| 2 | 2026-11-15 | [Two Sum](https://leetcode.com/problems/two-sum/): one-pass hash map | Arrays & Hashing | Complement lookup in a dict | Easy | 1 | [two-sum](two-sum/) |
| 3 | 2026-11-16 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/): string reversal, two pointers, reverse half | Math | Digit reversal with % and // | Easy | 3 | [palindrome-number](palindrome-number/) |
| 4 | 2026-11-17 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/): new list, two pointers | Two Pointers | Read/write pointers | Easy | 2 | [remove-duplicates-from-sorted-array](remove-duplicates-from-sorted-array/) |
| 5 | 2026-11-18 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/): in place, unsorted input | Two Pointers | Read/write pointers | Easy | 1 | [remove-duplicates-from-sorted-array](remove-duplicates-from-sorted-array/) |
| 5 | 2026-11-18 | [Plus One](https://leetcode.com/problems/plus-one/): string conversion | Math | Carry from the right | Easy | 1 | [plus-one](plus-one/) |
| 6 | 2026-11-19 | [Plus One](https://leetcode.com/problems/plus-one/): map, carry | Math | Carry from the right | Easy | 2 | [plus-one](plus-one/) |
| 6 | 2026-11-19 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/): nested loops, startswith | Strings | Vertical / horizontal scan | Easy | 2 | [longest-common-prefix](longest-common-prefix/) |
| 7 | 2026-11-20 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer/): single pass | Math | Value map + look-ahead | Easy | 1 | [roman-to-integer](roman-to-integer/) |
| 8 | 2026-11-21 | [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/): built-in method, for loop | Strings | Substring search: slide and compare | Easy | 2 | [find-the-index-of-the-first-occurrence-in-a-string](find-the-index-of-the-first-occurrence-in-a-string/) |

## How each folder is organized

```
problem-name/
├── solution_1_<name>.py        # first approach
├── solution_2_<name>.py        # each better approach in its own file
└── notes.md                    # problem, approach comparison, mistakes, key takeaway
```

[PYTHON_REFERENCE.md](PYTHON_REFERENCE.md) is a short cheat sheet of the less-common Python used in these solutions.

Re-solves (revisits) go in `problem-name/revisits/revisit_N_YYYY-MM-DD.py`: written from a blank file 7, 14 and 21 days after the first solve, with every approach as its own method (e.g. `twoSum_brute_force`, `twoSum_hash_map`) and the same tests run against each. Each problem's `notes.md` has a Revisits table.

Run any solution file directly to execute its tests:

```bash
python two-sum/solution_1_brute_force.py
```

## Topics

- Arrays & Hashing
- Math
- Two Pointers
- Strings
