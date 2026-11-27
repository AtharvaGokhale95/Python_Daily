"""
Contains Duplicate | Approach 2: Sort, then compare neighbours
Topic: Arrays & Hashing | Difficulty: Easy
https://leetcode.com/problems/contains-duplicate/

Given an integer list `nums`, return True if any value appears at least
twice in the list, and False if every element is distinct.

Rules for every approach:
- nums must be left unchanged (the tests check this).
- An empty list has no duplicates: return False.

Idea: Sort a copy of the list with sorted(nums). After sorting, equal values sit
next to each other, so one pass comparing each value with the one before it
finds any duplicate. sorted() returns a new list, so nums is left unchanged.
Time: O(n log n) for the sort, then O(n) for the pass | Space: O(n) for the sorted copy
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
        
         # empty list returns False
        if not nums:
            return False
        
        # sorted() returns a new list without updating the original array
        sorted_nums = sorted(nums)
    
        # Just the first element is always unique
        # Start iterating from the second element and then compare it to the previous one to check for duplicates
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i -1]:
                return True
        return False

    @staticmethod
    def _validate(nums: list[int]) -> None:
        if not isinstance(nums, list):
            raise TypeError(f"nums must be a list, got {type(nums).__name__}")
        if not all(isinstance(num, int) for num in nums):
            raise TypeError("Every element in nums must be an int")
