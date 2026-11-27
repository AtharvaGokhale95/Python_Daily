# Python_Daily

One Python DSA problem a day. For each problem I write a brute-force solution first, then optimize it step by step, with time and space complexity for every approach.

**Started:** Nov 14, 2026

**Roadmap:** [ROADMAP.md](ROADMAP.md) lists the 92 Python DSA problems (Set 1) I'm working through, grouped by pattern, plus 14 testing and A/B-testing problems I do 1–2 a week, with my progress.

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
| 9 | 2026-11-22 | [Add Binary](https://leetcode.com/problems/add-binary/): built-in conversion | Math | Carry from the right, base 2 | Easy | 1 | [add-binary](add-binary/) |
| 10 | 2026-11-23 | [Add Binary](https://leetcode.com/problems/add-binary/): padded carry | Math | Carry from the right, base 2 | Easy | 1 | [add-binary](add-binary/) |
| 11 | 2026-11-24 | [Add Binary](https://leetcode.com/problems/add-binary/): carry without padding | Math | Carry from the right, base 2 | Easy | 1 | [add-binary](add-binary/) |
| 11 | 2026-11-24 | Parse Log Lines (data Python): split | Strings | re / split parsing into records | Easy | 1 | [parse-log-lines](parse-log-lines/) |
| 12 | 2026-11-25 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/): brute force | Arrays & Hashing | Set membership | Easy | 1 | [contains-duplicate](contains-duplicate/) |
| 13 | 2026-11-26 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/): sort, then compare neighbours | Arrays & Hashing | Set membership | Easy | 1 | [contains-duplicate](contains-duplicate/) |

## How the repo is organized

```
Python_Daily/
├── helpers.py                  # loader: finds each problem's solution files + revisit methods
├── pytest.ini                  # tells pytest where helpers.py is
├── .github/workflows/tests.yml # runs pytest on every push
└── problem-name/
    ├── solution_1_<name>.py    # first approach: just the Solution class
    ├── solution_2_<name>.py    # each further approach in its own file
    ├── revisits/
    │   └── revisit_N_YYYY-MM-DD.py   # re-solve: one method per approach
    ├── test_problem_name.py    # tests every solution file and revisit method
    └── notes.md                # problem, approach comparison, mistakes, key takeaway
```

[PYTHON_REFERENCE.md](PYTHON_REFERENCE.md) is a short cheat sheet of the less-common Python used in these solutions.

Re-solves (revisits) go in `problem-name/revisits/revisit_N_YYYY-MM-DD.py`: written from a blank file 7, 14 and 21 days after the first solve (at most one revisit a day; clashes move to the next free day), with every approach as its own method (e.g. `twoSum_brute_force`, `twoSum_hash_map`). The problem's test file picks them up automatically. Each problem's `notes.md` has a Revisits table.

## Running the tests

```bash
pip install pytest
pytest                  # every problem
pytest two-sum          # one problem
pytest two-sum -v       # one line per approach and test case
```

Each `test_*.py` calls `approaches(__file__, "<methodName>")` from `helpers.py`, which imports every `solution_*.py` and every `revisits/revisit_*.py` method in that folder, so one set of test cases checks all of them. A starter that still raises `NotImplementedError` shows as skipped. GitHub Actions runs `pytest` on every push (see the Actions tab).

## Topics

- Arrays & Hashing
- Math
- Two Pointers
- Strings
