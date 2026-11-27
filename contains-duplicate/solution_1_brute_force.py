"""
Contains Duplicate | Approach 1: Brute force (compare every pair)
Topic: Arrays & Hashing | Difficulty: Easy
https://leetcode.com/problems/contains-duplicate/

Given an integer list `nums`, return True if any value appears at least
twice in the list, and False if every element is distinct.

Rules for every approach:
- nums must be left unchanged (the tests check this).
- An empty list has no duplicates: return False.

Idea: Check every pair (i, j) with i < j: the outer loop picks i, the inner loop
picks j from range(i + 1, len(nums)). Return True the moment nums[i] == nums[j];
if no pair matched, return False.
Time: O(n^2), n(n - 1) / 2 comparisons when there is no duplicate | Space: O(1)
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
        
        # nums is not a sorted array so for every i; j iterates over range (i + 1, len(nums))
        # return True -> the moment nums[i] == nums[j]
        # if no pair matched -> return False
        
        for i in range (len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
        

    @staticmethod
    def _validate(nums: list[int]) -> None:
        if not isinstance(nums, list):
            raise TypeError(f"nums must be a list, got {type(nums).__name__}")
        if not all(isinstance(num, int) for num in nums):
            raise TypeError("Every element in nums must be an int")
