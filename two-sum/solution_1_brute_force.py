"""
Day 1: Two Sum | Approach 1: Brute force
Topic: Arrays & Hashing | Difficulty: Easy
https://leetcode.com/problems/two-sum/

Given a list of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to `target`. Each input has exactly one
solution, and the same element may not be used twice.

Idea: Check every pair (i, j) with i < j and return the first pair whose
values add up to target.
Time: O(n^2) | Space: O(1)
"""

class Solution:
    def twoSum(self, nums:list[int], target:int) -> list[int]:
        """ Return [i,j] (i < j) where nums[i] + nums[j] == target
        
        Raises:
            TypeError: nums is not a list of ints, or target is not an int
            ValueError: no two numbers in nums add up to target
        """
        
        self._validate(nums, target)
        
        n = len(nums)
        for i in range(n -1):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        raise ValueError(f"No two numbers add up to target")
    
    @staticmethod
    def _validate(nums:list[int], target:int) -> None:
        # isinstance(value, type) asks whether a value is of a given type, and answers True or False
        if not isinstance(nums, list):
            raise TypeError(f"nums must be a list, got {type(nums).__name__}")
        if not isinstance(target, int):
            raise TypeError(f"target must be an integer, got {type(target).__name__}")
        if not all(isinstance(x, int) for x in nums):
            raise TypeError(f"Every element of nums must be an int")
