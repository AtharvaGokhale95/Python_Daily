# Roadmap — Set 1

92 Python DSA problems, grouped by pattern, to finish before applying for Data Scientist and Data Engineer roles. I solve them top to bottom, one group at a time: the easy problems teach the pattern's template, the mediums teach its variations. Most are LeetCode problems; the rest are data-Python problems (group-by, dedupe, sessionizing …), object-oriented Python exercises (classes, inheritance, exceptions, special methods) and data structures built from scratch. Machine learning is practised separately, not here.

**Progress:** 6 / 92 solved · 0 mastered

**Mastery rule:** every solved problem is re-solved from a blank file, without notes, 7, 14 and 21 days after I first solve it. Three clean re-solves = mastered; needing help restarts the schedule.

Status: ✅ solved · ⭐ mastered · 🔜 up next · ⬜ not started. `DS` / `DE` = mainly asked for that role. *(optional)* = lower priority for DS / DE interviews.

| # | Pattern group | Solved |
|--:|---|--:|
| 1 | [Math & Strings](#1-math--strings) | 4/10 |
| 2 | [Arrays & Hashing](#2-arrays--hashing) | 1/10 |
| 3 | [Two Pointers](#3-two-pointers) | 1/7 |
| 4 | [Sliding Window](#4-sliding-window) | 0/6 |
| 5 | [Prefix Sum](#5-prefix-sum) | 0/3 |
| 6 | [Object-Oriented Python](#6-object-oriented-python) | 0/9 |
| 7 | [Data Structures from Scratch](#7-data-structures-from-scratch) | 0/6 |
| 8 | [Stack](#8-stack) | 0/4 |
| 9 | [Binary Search](#9-binary-search) | 0/6 |
| 10 | [Sorting & Intervals](#10-sorting--intervals) | 0/5 |
| 11 | [Heap / Top-K](#11-heap--top-k) | 0/7 |
| 12 | [Linked List](#12-linked-list) | 0/5 |
| 13 | [Trees](#13-trees) | 0/7 |
| 14 | [Graphs](#14-graphs) | 0/3 |
| 15 | [1-D DP & Greedy](#15-1-d-dp--greedy) | 0/4 |

## 1. Math & Strings

**Spot it:** Digits with % and //, building or scanning a string, parsing text. · 4/10 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 1 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) · LC 9 | Digit reversal with % and // | Easy | ✅ | [palindrome-number](palindrome-number/) |
| 2 | [Plus One](https://leetcode.com/problems/plus-one/) · LC 66 | Carry from the right | Easy | ✅ | [plus-one](plus-one/) |
| 3 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) · LC 13 | Value map + look-ahead | Easy | ✅ | [roman-to-integer](roman-to-integer/) |
| 4 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) · LC 14 | Vertical / horizontal scan | Easy | ✅ | [longest-common-prefix](longest-common-prefix/) |
| 5 | [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) · LC 28 | Substring search: slide and compare | Easy | ⬜ |  |
| 6 | [Add Binary](https://leetcode.com/problems/add-binary/) · LC 67 | Carry from the right, base 2 | Easy | ⬜ |  |
| 7 | [Reverse Integer](https://leetcode.com/problems/reverse-integer/) · LC 7 | Digit reversal + overflow check | Medium | ⬜ |  |
| 8 | [String Compression](https://leetcode.com/problems/string-compression/) · LC 443 | Run-length encoding, read/write pointers | Medium | ⬜ |  |
| 9 | Parse Log Lines · data Python `DE` | re / split parsing into records | Easy | ⬜ |  |
| 10 | Descriptive Stats from Scratch · data Python `DS` | Mean, median, mode, std, percentile by hand | Easy | ⬜ |  |

## 2. Arrays & Hashing

**Spot it:** "Seen before?", "count", "group by" → dict, set, Counter. · 1/10 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 11 | [Two Sum](https://leetcode.com/problems/two-sum/) · LC 1 | Complement lookup in a dict | Easy | ✅ | [two-sum](two-sum/) |
| 12 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) · LC 217 | Set membership | Easy | ⬜ |  |
| 13 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) · LC 242 | Frequency count (Counter) | Easy | ⬜ |  |
| 14 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) · LC 49 | Group by a canonical key | Medium | ⬜ |  |
| 15 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) · LC 347 | Count + bucket sort | Medium | ⬜ |  |
| 16 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) · LC 238 | Prefix × suffix products | Medium | ⬜ |  |
| 17 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) · LC 128 | Set + start-of-run check | Medium | ⬜ |  |
| 18 | Group-by Aggregate · data Python | defaultdict sum / avg per key | Easy | ⬜ |  |
| 19 | Dedupe Records, Keep Latest · data Python `DE` | Dict by id, keep newest timestamp | Medium | ⬜ |  |
| 20 | Reservoir Sampling · data Python | Uniform sample from a stream | Medium | ⬜ |  |

## 3. Two Pointers

**Spot it:** Sorted input, pairs, in-place edits, palindromes. · 1/7 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 21 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) · LC 26 | Read/write pointers | Easy | ✅ | [remove-duplicates-from-sorted-array](remove-duplicates-from-sorted-array/) |
| 22 | [Remove Element](https://leetcode.com/problems/remove-element/) · LC 27 | Read/write pointers (filter in place) | Easy | ⬜ |  |
| 23 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) · LC 125 | Converging pointers | Easy | ⬜ |  |
| 24 | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) · LC 88 | Merge from the back | Easy | ⬜ |  |
| 25 | [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) · LC 167 | Converging pointers on sorted input | Medium | ⬜ |  |
| 26 | [3Sum](https://leetcode.com/problems/3sum/) · LC 15 | Sort + fix one + converge | Medium | ⬜ |  |
| 27 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) · LC 11 | Converge, move the shorter side | Medium | ⬜ |  |

## 4. Sliding Window

**Spot it:** Contiguous subarray/substring + longest, shortest, max or "at most k". · 0/6 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 28 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) · LC 121 | Running minimum | Easy | ⬜ |  |
| 29 | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) · LC 643 | Fixed-size window | Easy | ⬜ |  |
| 30 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) · LC 3 | Variable window + set | Medium | ⬜ |  |
| 31 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) · LC 424 | Variable window + counts | Medium | ⬜ |  |
| 32 | [Permutation in String](https://leetcode.com/problems/permutation-in-string/) · LC 567 | Fixed window + frequency match | Medium | ⬜ |  |
| 33 | Moving Average of a Stream · data Python | Fixed window with deque | Easy | ⬜ |  |

## 5. Prefix Sum

**Spot it:** Range sums, running totals, "subarray sums to k". · 0/3 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 34 | [Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) · LC 1480 | Cumulative sum | Easy | ⬜ |  |
| 35 | [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) · LC 724 | Total minus left sum | Easy | ⬜ |  |
| 36 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) · LC 560 | Prefix sum + dict of counts | Medium | ⬜ |  |

## 6. Object-Oriented Python

**Spot it:** Model things as classes: state + behaviour, inheritance, your own exceptions, Python's special methods. · 0/9 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 37 | Bank Account · OOP | Class, __init__, methods, @property, custom exception | Easy | ⬜ |  |
| 38 | Shape Hierarchy · OOP | Inheritance, abstract base class, super(), polymorphism | Easy | ⬜ |  |
| 39 | Employee Payroll · OOP | Class vs instance attributes, @classmethod, @staticmethod, overriding | Easy | ⬜ |  |
| 40 | Money Type with Dunder Methods · OOP | __repr__, __eq__, __add__, __lt__, __hash__ | Easy | ⬜ |  |
| 41 | Library Management System · OOP | Composition, custom exception hierarchy, try / except / else / finally | Medium | ⬜ |  |
| 42 | Custom Iterator and Generator · OOP | __iter__ / __next__, StopIteration, yield | Medium | ⬜ |  |
| 43 | Timer Context Manager · OOP | __enter__ / __exit__, handling exceptions on exit | Medium | ⬜ |  |
| 44 | Retry Decorator with Backoff · OOP `DE` | Decorators + exceptions | Medium | ⬜ |  |
| 45 | Parking Lot Design · OOP | Several classes, inheritance, Enum, exceptions | Medium | ⬜ |  |

## 7. Data Structures from Scratch

**Spot it:** Build the structure yourself: linked list, hash table, stack, queue, tree. · 0/6 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 46 | [Design Linked List](https://leetcode.com/problems/design-linked-list/) · LC 707 | Node class, head pointer, insert / delete at index | Medium | ⬜ |  |
| 47 | [Design HashMap](https://leetcode.com/problems/design-hashmap/) · LC 706 | Buckets + chaining, hash function | Easy | ⬜ |  |
| 48 | [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/) · LC 225 | Stack (LIFO) on top of a queue | Easy | ⬜ |  |
| 49 | [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) · LC 232 | Queue (FIFO) with two stacks, amortized O(1) | Easy | ⬜ |  |
| 50 | [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/) · LC 622 | Fixed-size list + head / tail indices | Medium | ⬜ |  |
| 51 | Binary Search Tree from Scratch · From scratch | Node class, insert, search, delete, traversals | Medium | ⬜ |  |

## 8. Stack

**Spot it:** Matching pairs, nesting, "next greater / warmer". · 0/4 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 52 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) · LC 20 | Match pairs with a stack | Easy | ⬜ |  |
| 53 | [Min Stack](https://leetcode.com/problems/min-stack/) · LC 155 | Auxiliary min stack | Medium | ⬜ |  |
| 54 | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) · LC 150 | Operand stack | Medium | ⬜ |  |
| 55 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) · LC 739 | Monotonic decreasing stack | Medium | ⬜ |  |

## 9. Binary Search

**Spot it:** Sorted input, "find the position", "smallest value that works", O(log n). · 0/6 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 56 | [Binary Search](https://leetcode.com/problems/binary-search/) · LC 704 | lo / hi template | Easy | ⬜ |  |
| 57 | [Search Insert Position](https://leetcode.com/problems/search-insert-position/) · LC 35 | Lower bound (first ≥ target) | Easy | ⬜ |  |
| 58 | [Sqrt(x)](https://leetcode.com/problems/sqrtx/) · LC 69 | Binary search on the answer | Easy | ⬜ |  |
| 59 | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) · LC 875 | Binary search on the answer | Medium | ⬜ |  |
| 60 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) · LC 33 | Find the sorted half | Medium | ⬜ |  |
| 61 | [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) · LC 981 `DE` | bisect on timestamps | Medium | ⬜ |  |

## 10. Sorting & Intervals

**Spot it:** Overlapping ranges, schedules, sessions → sort by start, then sweep. · 0/5 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 62 | [Sort Array by Increasing Frequency](https://leetcode.com/problems/sort-array-by-increasing-frequency/) · LC 1636 | Custom sort key | Easy | ⬜ |  |
| 63 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) · LC 56 | Sort by start + merge | Medium | ⬜ |  |
| 64 | [Insert Interval](https://leetcode.com/problems/insert-interval/) · LC 57 | Before / overlap / after sweep | Medium | ⬜ |  |
| 65 | [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) · LC 435 | Greedy by end time | Medium | ⬜ |  |
| 66 | Sessionize User Events · data Python | Sort by user + time, split on a gap | Medium | ⬜ |  |

## 11. Heap / Top-K

**Spot it:** "k largest / smallest / closest / most frequent", streaming median, merging sorted data. · 0/7 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 67 | [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) · LC 703 | Min-heap of size k | Easy | ⬜ |  |
| 68 | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) · LC 215 | heapq (or quickselect) | Medium | ⬜ |  |
| 69 | [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) · LC 973 | Heap keyed by distance | Medium | ⬜ |  |
| 70 | [Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/) · LC 692 | Counter + heap with tie-break | Medium | ⬜ |  |
| 71 | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) · LC 295 `DS` | Two heaps | Hard | ⬜ |  |
| 72 | Top-K Words in a Large File · data Python `DE` | Generator chunks + Counter.most_common | Medium | ⬜ |  |
| 73 | Merge Sorted Files · data Python `DE` | k-way merge with heapq.merge | Medium | ⬜ |  |

## 12. Linked List

**Spot it:** Node pointers: reverse, detect a cycle, merge. · 0/5 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 74 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) · LC 206 | prev / curr pointer flip | Easy | ⬜ |  |
| 75 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) · LC 21 | Dummy head merge | Easy | ⬜ |  |
| 76 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) · LC 141 | Fast / slow pointers | Easy | ⬜ |  |
| 77 | [LRU Cache](https://leetcode.com/problems/lru-cache/) · LC 146 `DE` | Dict + doubly linked list (OrderedDict) | Medium | ⬜ |  |
| 78 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) · LC 23 | Heap of list heads | Hard | ⬜ |  |

## 13. Trees

**Spot it:** Hierarchies and nested data, "depth", "level by level". · 0/7 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 79 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) · LC 104 | Recursive DFS | Easy | ⬜ |  |
| 80 | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) · LC 226 | Recursive swap | Easy | ⬜ |  |
| 81 | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) · LC 102 | BFS with a queue | Medium | ⬜ |  |
| 82 | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) · LC 98 | DFS with min / max bounds | Medium | ⬜ |  |
| 83 | [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) · LC 235 | Walk using the BST property | Medium | ⬜ |  |
| 84 | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) · LC 230 | In-order traversal | Medium | ⬜ |  |
| 85 | Flatten Nested JSON · data Python `DE` | Recursive DFS over dicts and lists | Medium | ⬜ |  |

## 14. Graphs

**Spot it:** Grids, connections, dependencies and run order. · 0/3 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 86 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) · LC 200 | Count components (DFS / BFS) | Medium | ⬜ |  |
| 87 | [Course Schedule](https://leetcode.com/problems/course-schedule/) · LC 207 | Cycle detection in a DAG | Medium | ⬜ |  |
| 88 | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) · LC 210 `DE` | Topological sort (Kahn's BFS) | Medium | ⬜ |  |

## 15. 1-D DP & Greedy

**Spot it:** "Number of ways", best total over choices, overlapping subproblems; greedy "farthest reach". Rarely asked for DS / DE beyond these. · 0/4 solved

| # | Problem | Pattern | Difficulty | Status | Solution |
|--:|---|---|---|:-:|---|
| 89 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) · LC 70 | Fibonacci-style DP | Easy | ⬜ |  |
| 90 | [House Robber](https://leetcode.com/problems/house-robber/) · LC 198 *(optional)* | Take / skip DP | Medium | ⬜ |  |
| 91 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) · LC 53 *(optional)* | Kadane's algorithm | Medium | ⬜ |  |
| 92 | [Jump Game](https://leetcode.com/problems/jump-game/) · LC 55 | Greedy farthest reach | Medium | ⬜ |  |
