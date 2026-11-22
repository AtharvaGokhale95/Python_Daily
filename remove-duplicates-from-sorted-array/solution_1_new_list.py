"""
Remove Duplicates from Sorted Array | Approach 1: New list (not in place)
Topic: Two Pointers | Difficulty: Easy
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given an integer list `nums` sorted in non-decreasing order, remove the
duplicates so each unique value appears once, keeping their relative order.
This version builds and returns a NEW list; `nums` is left unchanged.

Idea: Walk nums and append each value that isn't already in new_list.
Time: O(n^2) | Space: O(n)
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> list[int]:
        """Return a new list with each value of the sorted list nums once.

        Args:
            nums (list[int]): Sorted list to check; must be a list of ints.

        Raises:
            TypeError: nums is not a list of ints.

        Returns:
            A new list of the unique values, in order. nums is not changed.
        """
        self._validate(nums)
        
        new_list = []
        for i in range(len(nums)):
            if nums[i] in new_list:
                pass
            else:
                new_list.append(nums[i])
        return new_list
        

    @staticmethod
    def _validate(nums: list[int]) -> None:
        if not isinstance(nums, list):
            raise TypeError(f"nums must be a list, got {type(nums).__name__}")
        if not all(isinstance(num, int) for num in nums):
            raise TypeError("Every element in nums must be an int")
