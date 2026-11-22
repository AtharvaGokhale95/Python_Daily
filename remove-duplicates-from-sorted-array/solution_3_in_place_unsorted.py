"""
Remove Duplicates from Sorted Array | Approach 3: In place, unsorted input
Topic: Two Pointers | Difficulty: Easy
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given an integer list `nums` sorted in non-decreasing order, remove the
duplicates so each unique value appears once, keeping their relative order.
Extension: the input is NOT necessarily sorted. Remove duplicates in place,
keep the first occurrence of each value in its original order, and return k.

Idea: Keep a set of values already seen. Walk nums; copy each value not yet
seen to nums[write_idx] and move write_idx forward.
Time: O(n) | Space: O(n) for the set
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """Remove duplicates from nums in place.

        Args:
            nums (list[int]): List (sorted or not) to change in place; must be a list of ints.

        Raises:
            TypeError: nums is not a list of ints.

        Returns:
            k, the number of unique values. nums[:k] holds them in their
            original order; whatever is after index k doesn't matter.
        """
        self._validate(nums)
        
        seen = set()                            # create an empty set
        
        write_idx = 0                           # idx to write in-place in nums
        for num in nums:
            if num not in seen:                 # only if num is not in seen:
                seen.add(num)                   # num will be added to seen
                nums[write_idx] = num           # num will be updated at write_idx in nums
                write_idx += 1                  # write_idx is incremented
        return len(nums[: write_idx])
        
        # The following solution has a better memory complexity but does not retain the order
        # if len(nums) == 0:
        #     return 0
        
        # nums.sort()         # we first sort the array
        
        # write_idx = 1
        # for read_idx in range(1, len(nums)):
        #     if nums[read_idx] != nums[read_idx - 1]:
        #         nums[write_idx] = nums[read_idx]
        #         write_idx += 1
        # return write_idx

    @staticmethod
    def _validate(nums: list[int]) -> None:
        if not isinstance(nums, list):
            raise TypeError(f"nums must be a list, got {type(nums).__name__}")
        if not all(isinstance(num, int) for num in nums):
            raise TypeError("Every element in nums must be an int")
