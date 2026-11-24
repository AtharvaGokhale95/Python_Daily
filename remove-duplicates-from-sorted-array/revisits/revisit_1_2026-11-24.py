"""
Remove Duplicates from Sorted Array | Revisit 1 of 3 (due 2026-11-24)
Topic: Two Pointers | Difficulty: Easy
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given an integer list `nums` sorted in non-decreasing order, remove the
duplicates so each unique value appears once, keeping their relative order.

Re-solve EVERY approach from a blank file, without looking at earlier
solutions or notes. One method per approach; they can share `_validate`.
- new_list: return a NEW list of the unique values; leave nums unchanged.
- two_pointers: in place on sorted input; return k, unique values in nums[:k].
- in_place_unsorted: in place, input NOT necessarily sorted; keep the first
  occurrence of each value in its original order; return k.
Validation: raise TypeError when nums is not a list of ints.
Run the tests: pytest remove-duplicates-from-sorted-array -k revisit -v

Approach 1: New list                       | Time: O(?) | Space: O(?) | Result: TODO
Approach 2: Two pointers (in place, sorted) | Time: O(?) | Space: O(?) | Result: TODO
Approach 3: In place, unsorted input       | Time: O(?) | Space: O(?) | Result: TODO
"""


class Solution:
    def removeDuplicates_new_list(self, nums: list[int]) -> list[int]:
        """Approach 1: New list (nums unchanged)."""
        # TODO: write your solution here
        raise NotImplementedError

    def removeDuplicates_two_pointers(self, nums: list[int]) -> int:
        """Approach 2: Two pointers, in place, sorted input; returns k."""
        # TODO: write your solution here
        raise NotImplementedError

    def removeDuplicates_in_place_unsorted(self, nums: list[int]) -> int:
        """Approach 3: In place, unsorted input; returns k."""
        # TODO: write your solution here
        raise NotImplementedError

    @staticmethod
    def _validate(nums: list[int]) -> None:
        # TODO: raise TypeError for bad input types
        pass
