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


# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         """Return [i, j] (i < j) where nums[i] + nums[j] == target.

#         Raises:
#             TypeError: nums is not a list of ints, or target is not an int.
#             ValueError: no two numbers add up to target.
#         """
#         self._validate(nums, target)
#         n = len(nums)
#         for i in range(n - 1):
#             for j in range(i + 1, n):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         raise ValueError(f"No two numbers add up to {target}")

#     @staticmethod
#     def _validate(nums: list[int], target: int) -> None:
#         if not isinstance(nums, list):
#             raise TypeError(f"nums must be a list, got {type(nums).__name__}")
#         if not all(isinstance(x, int) for x in nums):
#             raise TypeError("Every element of nums must be an int")
#         if not isinstance(target, int):
#             raise TypeError(f"target must be an int, got {type(target).__name__}")


# if __name__ == "__main__":
#     s = Solution()

#     # (nums, target, expected)
#     cases = [
#         ([2, 7, 11, 15], 9, [0, 1]),          # basic
#         ([3, 2, 4], 6, [1, 2]),               # can't reuse index 0 (3+3)
#         ([3, 3], 6, [0, 1]),                  # duplicates
#         ([-1, -2, -3, -4, -5], -8, [2, 4]),   # negatives
#         ([0, 4, 3, 0], 0, [0, 3]),            # zeros
#     ]
#     for nums, target, expected in cases:
#         result = s.twoSum(nums, target)
#         assert result == expected, f"{nums}, {target}: got {result}, expected {expected}"

#     # (nums, target, expected exception)
#     bad_inputs = [
#         ([1, 2, 3], 100, ValueError),         # no solution
#         ([], 0, ValueError),                  # empty list
#         ("123", 3, TypeError),                # not a list
#         ([1, "2"], 3, TypeError),             # non-int element
#     ]
#     for nums, target, exc in bad_inputs:
#         try:
#             s.twoSum(nums, target)
#         except exc:
#             pass
#         else:
#             raise AssertionError(f"Expected {exc.__name__} for {nums!r}, {target!r}")

djjhkdjfklkjsdlkklk