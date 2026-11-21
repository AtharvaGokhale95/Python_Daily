# Roadmap — Set 1

87 Python DSA problems, grouped by pattern, to finish before applying for Data Scientist and Data Engineer roles. I solve them top to bottom, one group at a time: the easy problems teach the pattern's template, the mediums teach its variations. Most are LeetCode problems; the rest are data-Python problems (group-by, dedupe, sessionizing …), object-oriented Python exercises (classes, inheritance, exceptions, special methods) and data structures built from scratch. Machine learning is practised separately, not here.

**Progress:** 6 / 87 solved · 0 mastered

**Mastery rule:** every solved problem is re-solved from a blank file, without notes, 7, 14 and 21 days after I first solve it. Three clean re-solves = mastered; needing help restarts the schedule.

Status: ✅ solved · ⭐ mastered · 🔜 up next · ⬜ not started. `DS` / `DE` = mainly asked for that role. *(optional)* = lower priority for DS / DE interviews.

| # | Pattern group | Solved |
|--:|---|--:|
| 1 | [Math & Strings](#1-math--strings) | 4/8 |
| 2 | [Arrays & Hashing](#2-arrays--hashing) | 1/10 |
| 3 | [Two Pointers](#3-two-pointers) | 1/6 |
| 4 | [Sliding Window](#4-sliding-window) | 0/6 |
| 5 | [Prefix Sum](#5-prefix-sum) | 0/3 |
| 6 | [Object-Oriented Python](#6-object-oriented-python) | 0/9 |
| 7 | [Data Structures from Scratch](#7-data-structures-from-scratch) | 0/6 |
| 8 | [Stack](#8-stack) | 0/4 |
| 9 | [Binary Search](#9-binary-search) | 0/5 |
| 10 | [Sorting & Intervals](#10-sorting--intervals) | 0/5 |
| 11 | [Heap / Top-K](#11-heap--top-k) | 0/7 |
| 12 | [Linked List](#12-linked-list) | 0/5 |
| 13 | [Trees](#13-trees) | 0/7 |
| 14 | [Graphs](#14-graphs) | 0/3 |
| 15 | [1-D DP (optional)](#15-1-d-dp-optional) | 0/3 |

## 1. Math & Strings

**Spot it:** Digits with % and //, building or scanning a string, parsing text. · 4/8 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 1 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) · LC 9 | Digit reversal with % and // | Easy | ✅ | [palindrome-number](palindrome-number/) |
| 2 | [Plus One](https://leetcode.com/problems/plus-one/) · LC 66 | Carry from the right | Easy | ✅ | [plus-one](plus-one/) |
| 3 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) · LC 13 | Value map + look-ahead | Easy | ✅ | [roman-to-integer](roman-to-integer/) |
| 4 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) · LC 14 | Vertical / horizontal scan | Easy | ✅ | [longest-common-prefix](longest-common-prefix/) |
| 5 | [Reverse Integer](https://leetcode.com/problems/reverse-integer/) · LC 7 | Digit reversal + overflow check | Medium | ⬜ |  |
| 6 | [String Compression](https://leetcode.com/problems/string-compression/) · LC 443 | Run-length encoding, read/write pointers | Medium | ⬜ |  |
| 7 | Parse Log Lines · data Python `DE` | re / split parsing into records | Easy | ⬜ |  |
| 8 | Descriptive Stats from Scratch · data Python `DS` | Mean, median, mode, std, percentile by hand | Easy | ⬜ |  |

## 2. Arrays & Hashing

**Spot it:** "Seen before?", "count", "group by" → dict, set, Counter. · 1/10 solved

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
| 18 | Reservoir Sampling · data Python | Uniform sample from a stream | Medium | ⬜ |  |

## 3. Two Pointers

**Spot it:** Sorted input, pairs, in-place edits, palindromes. · 1/6 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 19 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) · LC 26 | Read/write pointers | Easy | ✅ | [remove-duplicates-from-sorted-array](remove-duplicates-from-sorted-array/) |
| 20 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) · LC 125 | Converging pointers | Easy | ⬜ |  |
| 21 | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) · LC 88 | Merge from the back | Easy | ⬜ |  |
| 22 | [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) · LC 167 | Converging pointers on sorted input | Medium | ⬜ |  |
| 23 | [3Sum](https://leetcode.com/problems/3sum/) · LC 15 | Sort + fix one + converge | Medium | ⬜ |  |
| 24 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) · LC 11 | Converge, move the shorter side | Medium | ⬜ |  |

## 4. Sliding Window

**Spot it:** Contiguous subarray/substring + longest, shortest, max or "at most k". · 0/6 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 25 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) · LC 121 | Running minimum | Easy | ⬜ |  |
| 26 | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) · LC 643 | Fixed-size window | Easy | ⬜ |  |
| 27 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) · LC 3 | Variable window + set | Medium | ⬜ |  |
| 28 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) · LC 424 | Variable window + counts | Medium | ⬜ |  |
| 29 | [Permutation in String](https://leetcode.com/problems/permutation-in-string/) · LC 567 | Fixed window + frequency match | Medium | ⬜ |  |
| 30 | Moving Average of a Stream · data Python | Fixed window with deque | Easy | ⬜ |  |

## 5. Prefix Sum

**Spot it:** Range sums, running totals, "subarray sums to k". · 0/3 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 31 | [Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) · LC 1480 | Cumulative sum | Easy | ⬜ |  |
| 32 | [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) · LC 724 | Total minus left sum | Easy | ⬜ |  |
| 33 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) · LC 560 | Prefix sum + dict of counts | Medium | ⬜ |  |

## 6. Object-Oriented Python

**Spot it:** Model things as classes: state + behaviour, inheritance, your own exceptions, Python's special methods. · 0/9 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 34 | Bank Account · OOP | Class, __init__, methods, @property, custom exception | Easy | ⬜ |  |
| 35 | Shape Hierarchy · OOP | Inheritance, abstract base class, super(), polymorphism | Easy | ⬜ |  |
| 36 | Employee Payroll · OOP | Class vs instance attributes, @classmethod, @staticmethod, overriding | Easy | ⬜ |  |
| 37 | Money Type with Dunder Methods · OOP | __repr__, __eq__, __add__, __lt__, __hash__ | Easy | ⬜ |  |
| 38 | Library Management System · OOP | Composition, custom exception hierarchy, try / except / else / finally | Medium | ⬜ |  |
| 39 | Custom Iterator and Generator · OOP | __iter__ / __next__, StopIteration, yield | Medium | ⬜ |  |
| 40 | Timer Context Manager · OOP | __enter__ / __exit__, handling exceptions on exit | Medium | ⬜ |  |
| 41 | Retry Decorator with Backoff · OOP `DE` | Decorators + exceptions | Medium | ⬜ |  |
| 42 | Parking Lot Design · OOP | Several classes, inheritance, Enum, exceptions | Medium | ⬜ |  |

## 7. Data Structures from Scratch

**Spot it:** Build the structure yourself: linked list, hash table, stack, queue, tree. · 0/6 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 43 | [Design Linked List](https://leetcode.com/problems/design-linked-list/) · LC 707 | Node class, head pointer, insert / delete at index | Medium | ⬜ |  |
| 44 | [Design HashMap](https://leetcode.com/problems/design-hashmap/) · LC 706 | Buckets + chaining, hash function | Easy | ⬜ |  |
| 45 | [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/) · LC 225 | Stack (LIFO) on top of a queue | Easy | ⬜ |  |
| 46 | [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) · LC 232 | Queue (FIFO) with two stacks, amortized O(1) | Easy | ⬜ |  |
| 47 | [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/) · LC 622 | Fixed-size list + head / tail indices | Medium | ⬜ |  |
| 48 | Binary Search Tree from Scratch · From scratch | Node class, insert, search, delete, traversals | Medium | ⬜ |  |

## 8. Stack

**Spot it:** Matching pairs, nesting, "next greater / warmer". · 0/4 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 49 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) · LC 20 | Match pairs with a stack | Easy | ⬜ |  |
| 50 | [Min Stack](https://leetcode.com/problems/min-stack/) · LC 155 | Auxiliary min stack | Medium | ⬜ |  |
| 51 | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) · LC 150 | Operand stack | Medium | ⬜ |  |
| 52 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) · LC 739 | Monotonic decreasing stack | Medium | ⬜ |  |

## 9. Binary Search

**Spot it:** Sorted input, "find the position", "smallest value that works", O(log n). · 0/5 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 53 | [Binary Search](https://leetcode.com/problems/binary-search/) · LC 704 | lo / hi template | Easy | ⬜ |  |
| 54 | [Search Insert Position](https://leetcode.com/problems/search-insert-position/) · LC 35 | Lower bound (first ≥ target) | Easy | ⬜ |  |
| 55 | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) · LC 875 | Binary search on the answer | Medium | ⬜ |  |
| 56 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) · LC 33 | Find the sorted half | Medium | ⬜ |  |
| 57 | [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) · LC 981 `DE` | bisect on timestamps | Medium | ⬜ |  |

## 10. Sorting & Intervals

**Spot it:** Overlapping ranges, schedules, sessions → sort by start, then sweep. · 0/5 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 58 | [Sort Array by Increasing Frequency](https://leetcode.com/problems/sort-array-by-increasing-frequency/) · LC 1636 | Custom sort key | Easy | ⬜ |  |
| 59 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) · LC 56 | Sort by start + merge | Medium | ⬜ |  |
| 60 | [Insert Interval](https://leetcode.com/problems/insert-interval/) · LC 57 | Before / overlap / after sweep | Medium | ⬜ |  |
| 61 | [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) · LC 435 | Greedy by end time | Medium | ⬜ |  |
| 62 | Sessionize User Events · data Python | Sort by user + time, split on a gap | Medium | ⬜ |  |

## 11. Heap / Top-K

**Spot it:** "k largest / smallest / closest / most frequent", streaming median, merging sorted data. · 0/7 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 63 | [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) · LC 703 | Min-heap of size k | Easy | ⬜ |  |
| 64 | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) · LC 215 | heapq (or quickselect) | Medium | ⬜ |  |
| 65 | [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) · LC 973 | Heap keyed by distance | Medium | ⬜ |  |
| 66 | [Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/) · LC 692 | Counter + heap with tie-break | Medium | ⬜ |  |
| 67 | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) · LC 295 `DS` | Two heaps | Hard | ⬜ |  |
| 68 | Top-K Words in a Large File · data Python `DE` | Generator chunks + Counter.most_common | Medium | ⬜ |  |
| 69 | Merge Sorted Files · data Python `DE` | k-way merge with heapq.merge | Medium | ⬜ |  |

## 12. Linked List

**Spot it:** Node pointers: reverse, detect a cycle, merge. · 0/5 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 70 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) · LC 206 | prev / curr pointer flip | Easy | ⬜ |  |
| 71 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) · LC 21 | Dummy head merge | Easy | ⬜ |  |
| 72 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) · LC 141 | Fast / slow pointers | Easy | ⬜ |  |
| 73 | [LRU Cache](https://leetcode.com/problems/lru-cache/) · LC 146 `DE` | Dict + doubly linked list (OrderedDict) | Medium | ⬜ |  |
| 74 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) · LC 23 | Heap of list heads | Hard | ⬜ |  |

## 13. Trees

**Spot it:** Hierarchies and nested data, "depth", "level by level". · 0/7 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 75 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) · LC 104 | Recursive DFS | Easy | ⬜ |  |
| 76 | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) · LC 226 | Recursive swap | Easy | ⬜ |  |
| 77 | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) · LC 102 | BFS with a queue | Medium | ⬜ |  |
| 78 | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) · LC 98 | DFS with min / max bounds | Medium | ⬜ |  |
| 79 | [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) · LC 235 | Walk using the BST property | Medium | ⬜ |  |
| 80 | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) · LC 230 | In-order traversal | Medium | ⬜ |  |
| 81 | Flatten Nested JSON · data Python `DE` | Recursive DFS over dicts and lists | Medium | ⬜ |  |

## 14. Graphs

**Spot it:** Grids, connections, dependencies and run order. · 0/3 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 82 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) · LC 200 | Count components (DFS / BFS) | Medium | ⬜ |  |
| 83 | [Course Schedule](https://leetcode.com/problems/course-schedule/) · LC 207 | Cycle detection in a DAG | Medium | ⬜ |  |
| 84 | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) · LC 210 `DE` | Topological sort (Kahn's BFS) | Medium | ⬜ |  |

## 15. 1-D DP (optional)

**Spot it:** "Number of ways", best total over choices, overlapping subproblems. Rarely asked for DS / DE beyond these. · 0/3 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 85 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) · LC 70 *(optional)* | Fibonacci-style DP | Easy | ⬜ |  |
| 86 | [House Robber](https://leetcode.com/problems/house-robber/) · LC 198 *(optional)* | Take / skip DP | Medium | ⬜ |  |
| 87 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) · LC 53 *(optional)* | Kadane's algorithm | Medium | ⬜ |  |
