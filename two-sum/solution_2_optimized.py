"""
Day 002 - Two Sum (Arrays & Hashing) | Approach 2: One-pass hash map.
Topic: Arrays & Hashing | Difficulty: Easy
https://leetcode.com/problems/two-sum/

Given a list of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to `target`. Each input has exactly one
solution, and the same element may not be used twice.

Idea: for each number, the partner it needs is (target - num).
Keep a dict of numbers already seen -> their index. If the partner
is already in the dict, we found the pair. Otherwise, store the
current number and move on.

Time: O(n)   Space: O(n)
"""

# Docstring Raises:	Promises what will happen
# _validate	Makes it happen
# Test except	Proves it happens, and keeps proving it after every change

class Solution:
    def twoSum(self, nums:list[int], target:int) -> list[int]:
        """Return [i, j] (i < j) where nums[i] + nums[j] == target

        Args:
            nums (list[int]): Value to check; must be a list of ints.
            target (int): Value to check; must be an int.

        Raises:
            TypeError: nums is not a list of int or target is not an int
            ValueError: no two numbers in nums add up to target

        Returns:
            A list of intergers which includes the indices of nums
        """
        self._validate(nums, target)                # Checks on nums and target for TypeError
        
        seen: dict[int, int] = {}   # 
        # key: number visited in nums
        # value: index of the that number
        
        # for index, item in enumerate(iterable, start=0)
        for i, num in enumerate(nums):
            complement = target - num           # the partner num needs
            if complement in seen:              # was the partner seen earlier?
                return [seen[complement], i]
            seen[num] = i                       # store AFTER checking, so num can't pair with itself
        raise ValueError(f"No two numbers in nums add up to {target}")       
        
    @staticmethod
    def _validate(nums:list[int], target: int) -> None:
        if not isinstance(nums, list):
            raise TypeError(f"nums must be a list, got {type(nums).__name__}")
        if not all(isinstance(num, int) for num in nums):
            raise TypeError(f"Every element in nums must be an int")
        if not isinstance(target, int):
            raise TypeError(f"target must be an int, got {type(target).__name__}")
