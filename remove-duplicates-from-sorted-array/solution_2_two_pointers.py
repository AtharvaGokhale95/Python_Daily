"""
Remove Duplicates from Sorted Array | Approach 2: Two pointers (in place, sorted)
Topic: Two Pointers | Difficulty: Easy
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given an integer list `nums` sorted in non-decreasing order, remove the
duplicates so each unique value appears once, keeping their relative order.
Do it in place with O(1) extra space and return k, the number of unique
values; the first k slots of `nums` must hold them.

Idea: A write pointer marks where the next unique value goes; a read pointer
scans from index 1 and copies each value that differs from the one before it.
Time: O(n) | Space: O(1)
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """Remove duplicates from nums in place.

        Args:
            nums (list[int]): Sorted list to change in place; must be a list of ints.

        Raises:
            TypeError: nums is not a list of ints.

        Returns:
            k, the number of unique values. nums[:k] holds them in their
            original order; whatever is after index k doesn't matter.
        """
        self._validate(nums)
        
        if len(nums) == 0:
            return 0
        
        # if the list is the not empty, there will be at least 1 unique element at idx = 0; so we will start writing the next unique element from idx = 1 and also read the nums from idx = 1
        write_idx = 1
        for read_idx in range(1, len(nums)):
            if nums[read_idx] != nums[read_idx -1]:     # check only if the current value is not equal to the previous one
                nums[write_idx] = nums[read_idx]
                write_idx += 1
        return write_idx                                # when we update the nums in-place, the len(nums) still remains the same; only the first write_idx values are unique

    @staticmethod
    def _validate(nums: list[int]) -> None:
        if not isinstance(nums, list):
            raise TypeError(f"nums must be a list, got {type(nums).__name__}")
        if not all(isinstance(num, int) for num in nums):
            raise TypeError("Every element in nums must be an int")
