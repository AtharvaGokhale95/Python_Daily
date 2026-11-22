"""
Two Sum | Revisit 1 of 3 (due 2026-11-21)
Topic: Arrays & Hashing | Difficulty: Easy
https://leetcode.com/problems/two-sum/

Given a list of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to `target`. Each input has exactly one
solution, and the same element may not be used twice.

Re-solve EVERY approach from a blank file, without looking at earlier
solutions or notes. One method per approach; they can share `_validate`.
Validation: raise TypeError for a non-list / non-int input, ValueError when
no pair exists.

Approach 1: Brute force       | Time: O(n^2) | Space: O(1) | Result: needed help (inner loop started at 1, not i + 1; _validate not called)
Approach 2: Hash map          | Time: O(n)   | Space: O(n) | Result: needed help (_validate not called)
Both issues found in review on 2026-11-21 and fixed by Atharva the same day.
"""


class Solution:
    def twoSum_brute_force(self, nums: list[int], target: int) -> list[int]:
        
        self._validate(nums, target)
        
        """Approach 1: Brute force."""
        for i in range(len(nums)):
            compliment = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == compliment:
                    return [i, j]
        raise ValueError("No two numbers add up to the target")
                

    def twoSum_hash_map(self, nums: list[int], target: int) -> list[int]:
        
        self._validate(nums, target)
        
        """Approach 2: Hash map (one pass)."""
        seen_dict = {}
        # enumerate() gives index, value at the same time 
        for idx, value in enumerate(nums):
            compliment = target - value
            if compliment in seen_dict: 
                return [seen_dict[compliment], idx]         # the order of idx: smaller, larger: thus seen_dict[compliment], idx
            seen_dict[value] = idx
        raise ValueError("No two numbers add up to the target")
            

    @staticmethod
    def _validate(nums: list[int], target: int) -> None:
        if not isinstance(nums, list):
            raise TypeError(f"nums must be a list, got {type(nums).__name__}")
        if not isinstance(target, int):
            raise TypeError(f"target should be an integer, got {type(target).__name__}")
        if not all(isinstance(x, int) for x in nums):
            raise TypeError(f"every value in nums should be integer")
