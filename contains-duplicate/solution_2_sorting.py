"""
Contains Duplicate | Approach 2: Sort, then compare neighbours
Topic: Arrays & Hashing | Difficulty: Easy
https://leetcode.com/problems/contains-duplicate/

Given an integer list `nums`, return True if any value appears at least
twice in the list, and False if every element is distinct.

Rules for every approach:
- nums must be left unchanged (the tests check this).
- An empty list has no duplicates: return False.

Idea: TODO (sort a COPY with sorted(nums), because nums.sort() would change the caller's list; after sorting, equal values sit next to each other, so compare each value with the one before it)
Time: O(?) | Space: O(?)
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """Return True if any value appears at least twice in nums.

        Args:
            nums (list[int]): Integers; may be empty. Must not be modified.

        Raises:
            TypeError: nums is not a list of ints.

        Returns:
            True if some value appears two or more times, otherwise False.
        """
        self._validate(nums)
        # TODO: write your solution here
        raise NotImplementedError

    @staticmethod
    def _validate(nums: list[int]) -> None:
        if not isinstance(nums, list):
            raise TypeError(f"nums must be a list, got {type(nums).__name__}")
        if not all(isinstance(num, int) for num in nums):
            raise TypeError("Every element in nums must be an int")
