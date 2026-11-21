# Roadmap — Set 1

80 problems, grouped by pattern, to finish before applying for Data Scientist and Data Engineer roles. I solve them top to bottom, one group at a time: the easy problems teach the pattern's template, the mediums teach its variations. 66 are LeetCode problems; 14 are data-Python problems (the kind DS/DE interviews ask: group-by, dedupe, sessionizing, k-means …) placed in the group whose pattern they use.

**Progress:** 5 / 80 solved · 0 mastered

**Mastery rule:** every solved problem is re-solved from a blank file, without notes, 3 days later, then 7 days after that, then 21. Three clean re-solves = mastered; needing help restarts the schedule.

Status: ✅ solved · ⭐ mastered · 🔜 up next · ⬜ not started. `DS` / `DE` = mainly asked for that role.

| # | Pattern group | Solved |
|--:|---|--:|
| 1 | [Math & Strings](#1-math--strings) | 3/8 |
| 2 | [Arrays & Hashing](#2-arrays--hashing) | 1/9 |
| 3 | [Two Pointers](#3-two-pointers) | 1/6 |
| 4 | [Sliding Window](#4-sliding-window) | 0/6 |
| 5 | [Prefix Sum](#5-prefix-sum) | 0/3 |
| 6 | [Stack](#6-stack) | 0/4 |
| 7 | [Binary Search](#7-binary-search) | 0/5 |
| 8 | [Sorting & Intervals](#8-sorting--intervals) | 0/5 |
| 9 | [Heap / Top-K](#9-heap--top-k) | 0/7 |
| 10 | [Linked List](#10-linked-list) | 0/5 |
| 11 | [Trees](#11-trees) | 0/7 |
| 12 | [Graphs](#12-graphs) | 0/5 |
| 13 | [1-D DP & Greedy](#13-1-d-dp--greedy) | 0/5 |
| 14 | [Data & ML from Scratch](#14-data--ml-from-scratch) | 0/5 |

## 1. Math & Strings

**Spot it:** Digits with % and //, building or scanning a string, parsing text. · 3/8 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 1 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) · LC 9 | Digit reversal with % and // | Easy | ✅ | [palindrome-number](palindrome-number/) |
| 2 | [Plus One](https://leetcode.com/problems/plus-one/) · LC 66 | Carry from the right | Easy | ✅ | [plus-one](plus-one/) |
| 3 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) · LC 13 | Value map + look-ahead | Easy | 🔜 | [roman-to-integer](roman-to-integer/) |
| 4 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) · LC 14 | Vertical / horizontal scan | Easy | ✅ | [longest-common-prefix](longest-common-prefix/) |
| 5 | [Reverse Integer](https://leetcode.com/problems/reverse-integer/) · LC 7 | Digit reversal + overflow check | Medium | ⬜ |  |
| 6 | [String Compression](https://leetcode.com/problems/string-compression/) · LC 443 | Run-length encoding, read/write pointers | Medium | ⬜ |  |
| 7 | Parse Log Lines · data Python `DE` | re / split parsing into records | Easy | ⬜ |  |
| 8 | Descriptive Stats from Scratch · data Python `DS` | Mean, median, mode, std, percentile by hand | Easy | ⬜ |  |

## 2. Arrays & Hashing

**Spot it:** "Seen before?", "count", "group by" → dict, set, Counter. · 1/9 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 9 | [Two Sum](https://leetcode.com/problems/two-sum/) · LC 1 | Complement lookup in a dict | Easy | ✅ | [two-sum](two-sum/) |
| 10 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) · LC 217 | Set membership | Easy | ⬜ |  |
| 11 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) · LC 242 | Frequency count (Counter) | Easy | ⬜ |  |
| 12 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) · LC 49 | Group by a canonical key | Medium | ⬜ |  |
| 13 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) · LC 347 | Count + bucket sort | Medium | ⬜ |  |
| 14 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) · LC 238 | Prefix × suffix products | Medium | ⬜ |  |
| 15 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) · LC 128 | Set + start-of-run check | Medium | ⬜ |  |
| 16 | Group-by Aggregate · data Python | defaultdict sum / avg per key | Easy | ⬜ |  |
| 17 | Dedupe Records, Keep Latest · data Python `DE` | Dict by id, keep newest timestamp | Medium | ⬜ |  |

## 3. Two Pointers

**Spot it:** Sorted input, pairs, in-place edits, palindromes. · 1/6 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 18 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) · LC 26 | Read/write pointers | Easy | ✅ | [remove-duplicates-from-sorted-array](remove-duplicates-from-sorted-array/) |
| 19 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) · LC 125 | Converging pointers | Easy | ⬜ |  |
| 20 | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) · LC 88 | Merge from the back | Easy | ⬜ |  |
| 21 | [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) · LC 167 | Converging pointers on sorted input | Medium | ⬜ |  |
| 22 | [3Sum](https://leetcode.com/problems/3sum/) · LC 15 | Sort + fix one + converge | Medium | ⬜ |  |
| 23 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) · LC 11 | Converge, move the shorter side | Medium | ⬜ |  |

## 4. Sliding Window

**Spot it:** Contiguous subarray/substring + longest, shortest, max or "at most k". · 0/6 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 24 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) · LC 121 | Running minimum | Easy | ⬜ |  |
| 25 | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) · LC 643 | Fixed-size window | Easy | ⬜ |  |
| 26 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) · LC 3 | Variable window + set | Medium | ⬜ |  |
| 27 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) · LC 424 | Variable window + counts | Medium | ⬜ |  |
| 28 | [Permutation in String](https://leetcode.com/problems/permutation-in-string/) · LC 567 | Fixed window + frequency match | Medium | ⬜ |  |
| 29 | Moving Average of a Stream · data Python | Fixed window with deque | Easy | ⬜ |  |

## 5. Prefix Sum

**Spot it:** Range sums, running totals, "subarray sums to k". · 0/3 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 30 | [Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) · LC 1480 | Cumulative sum | Easy | ⬜ |  |
| 31 | [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) · LC 724 | Total minus left sum | Easy | ⬜ |  |
| 32 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) · LC 560 | Prefix sum + dict of counts | Medium | ⬜ |  |

## 6. Stack

**Spot it:** Matching pairs, nesting, "next greater / warmer". · 0/4 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 33 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) · LC 20 | Match pairs with a stack | Easy | ⬜ |  |
| 34 | [Min Stack](https://leetcode.com/problems/min-stack/) · LC 155 | Auxiliary min stack | Medium | ⬜ |  |
| 35 | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) · LC 150 | Operand stack | Medium | ⬜ |  |
| 36 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) · LC 739 | Monotonic decreasing stack | Medium | ⬜ |  |

## 7. Binary Search

**Spot it:** Sorted input, "find the position", "smallest value that works", O(log n). · 0/5 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 37 | [Binary Search](https://leetcode.com/problems/binary-search/) · LC 704 | lo / hi template | Easy | ⬜ |  |
| 38 | [Search Insert Position](https://leetcode.com/problems/search-insert-position/) · LC 35 | Lower bound (first ≥ target) | Easy | ⬜ |  |
| 39 | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) · LC 875 | Binary search on the answer | Medium | ⬜ |  |
| 40 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) · LC 33 | Find the sorted half | Medium | ⬜ |  |
| 41 | [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) · LC 981 `DE` | bisect on timestamps | Medium | ⬜ |  |

## 8. Sorting & Intervals

**Spot it:** Overlapping ranges, schedules, sessions → sort by start, then sweep. · 0/5 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 42 | [Sort Array by Increasing Frequency](https://leetcode.com/problems/sort-array-by-increasing-frequency/) · LC 1636 | Custom sort key | Easy | ⬜ |  |
| 43 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) · LC 56 | Sort by start + merge | Medium | ⬜ |  |
| 44 | [Insert Interval](https://leetcode.com/problems/insert-interval/) · LC 57 | Before / overlap / after sweep | Medium | ⬜ |  |
| 45 | [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) · LC 435 | Greedy by end time | Medium | ⬜ |  |
| 46 | Sessionize User Events · data Python | Sort by user + time, split on a gap | Medium | ⬜ |  |

## 9. Heap / Top-K

**Spot it:** "k largest / smallest / closest / most frequent", streaming median, merging sorted data. · 0/7 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 47 | [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) · LC 703 | Min-heap of size k | Easy | ⬜ |  |
| 48 | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) · LC 215 | heapq (or quickselect) | Medium | ⬜ |  |
| 49 | [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) · LC 973 | Heap keyed by distance | Medium | ⬜ |  |
| 50 | [Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/) · LC 692 | Counter + heap with tie-break | Medium | ⬜ |  |
| 51 | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) · LC 295 `DS` | Two heaps | Hard | ⬜ |  |
| 52 | Top-K Words in a Large File · data Python `DE` | Generator chunks + Counter.most_common | Medium | ⬜ |  |
| 53 | Merge Sorted Files · data Python `DE` | k-way merge with heapq.merge | Medium | ⬜ |  |

## 10. Linked List

**Spot it:** Node pointers: reverse, detect a cycle, merge. · 0/5 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 54 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) · LC 206 | prev / curr pointer flip | Easy | ⬜ |  |
| 55 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) · LC 21 | Dummy head merge | Easy | ⬜ |  |
| 56 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) · LC 141 | Fast / slow pointers | Easy | ⬜ |  |
| 57 | [LRU Cache](https://leetcode.com/problems/lru-cache/) · LC 146 `DE` | Dict + doubly linked list (OrderedDict) | Medium | ⬜ |  |
| 58 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) · LC 23 | Heap of list heads | Hard | ⬜ |  |

## 11. Trees

**Spot it:** Hierarchies and nested data, "depth", "level by level". · 0/7 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 59 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) · LC 104 | Recursive DFS | Easy | ⬜ |  |
| 60 | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) · LC 226 | Recursive swap | Easy | ⬜ |  |
| 61 | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) · LC 102 | BFS with a queue | Medium | ⬜ |  |
| 62 | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) · LC 98 | DFS with min / max bounds | Medium | ⬜ |  |
| 63 | [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) · LC 235 | Walk using the BST property | Medium | ⬜ |  |
| 64 | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) · LC 230 | In-order traversal | Medium | ⬜ |  |
| 65 | Flatten Nested JSON · data Python `DE` | Recursive DFS over dicts and lists | Medium | ⬜ |  |

## 12. Graphs

**Spot it:** Grids, connections, dependencies and run order. · 0/5 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 66 | [Flood Fill](https://leetcode.com/problems/flood-fill/) · LC 733 | Grid DFS | Easy | ⬜ |  |
| 67 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) · LC 200 | Count components (DFS / BFS) | Medium | ⬜ |  |
| 68 | [Clone Graph](https://leetcode.com/problems/clone-graph/) · LC 133 | DFS + dict of copies | Medium | ⬜ |  |
| 69 | [Course Schedule](https://leetcode.com/problems/course-schedule/) · LC 207 | Cycle detection in a DAG | Medium | ⬜ |  |
| 70 | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) · LC 210 `DE` | Topological sort (Kahn's BFS) | Medium | ⬜ |  |

## 13. 1-D DP & Greedy

**Spot it:** "Number of ways", best total over choices, overlapping subproblems. · 0/5 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 71 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) · LC 70 | Fibonacci-style DP | Easy | ⬜ |  |
| 72 | [House Robber](https://leetcode.com/problems/house-robber/) · LC 198 | Take / skip DP | Medium | ⬜ |  |
| 73 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) · LC 53 | Kadane's algorithm | Medium | ⬜ |  |
| 74 | [Coin Change](https://leetcode.com/problems/coin-change/) · LC 322 | Unbounded DP (fewest coins) | Medium | ⬜ |  |
| 75 | [Jump Game](https://leetcode.com/problems/jump-game/) · LC 55 | Greedy farthest reach | Medium | ⬜ |  |

## 14. Data & ML from Scratch

**Spot it:** Write by hand what pandas, scikit-learn or Airflow would do for you. · 0/5 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 76 | Reservoir Sampling · data Python | Uniform sample from a stream | Medium | ⬜ |  |
| 77 | Retry Decorator with Backoff · data Python `DE` | Decorators + exceptions | Medium | ⬜ |  |
| 78 | Classification Metrics from Scratch · data Python `DS` | Confusion matrix, precision, recall, F1 | Easy | ⬜ |  |
| 79 | Linear Regression with Gradient Descent · data Python `DS` | NumPy vectorization | Medium | ⬜ |  |
| 80 | k-Means Clustering from Scratch · data Python `DS` | NumPy, assign / update loop | Medium | ⬜ |  |
