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


if __name__ == "__main__":
    s = Solution()

    # (nums, expected first k values)
    cases = [
        ([1, 1, 2], [1, 2]),                          # basic
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]),  # LeetCode example 2
        ([], []),                                     # empty list
        ([5], [5]),                                   # single element
        ([1, 2, 3], [1, 2, 3]),                       # no duplicates
        ([2, 2, 2, 2], [2]),                          # all the same
        ([-3, -3, -1, 0, 0], [-3, -1, 0]),            # negatives and zero
        ([1, 1, 2, 3, 3], [1, 2, 3]),                 # duplicates at both ends
        ([3, 1, 3, 2, 1], [3, 1, 2]),                 # unsorted
        ([4, 4, 1, 4, 1], [4, 1]),                    # unsorted, repeats far apart
        ([0, -1, 0, -1, 2], [0, -1, 2]),              # unsorted with negatives
    ]
    for nums, expected in cases:
        before = list(nums)                 # keep a copy to show in the output
        k = s.removeDuplicates(nums)        # changes nums in place
        assert k == len(expected) and nums[:k] == expected, f"{before!r}: got k={k}, nums[:k]={nums[:k]}, expected {expected}"
        print(f"PASS nums = {before!r} -> No of unique values = {k}, nums[:k] = {nums[:k]}")

    # (nums, expected exception)
    bad_inputs = [
        ("112", TypeError),     # string, not a list
        ([1, "2"], TypeError),  # non-int element
        (None, TypeError),      # missing value
    ]
    for nums, exc in bad_inputs:
        try:
            result = s.removeDuplicates(nums)
        except exc as e:
            print(f"PASS nums = {nums!r} -> {exc.__name__}: {e}")
        else:
            raise AssertionError(f"FAIL nums = {nums!r} -> returned {result}, expected {exc.__name__}")

    print("All tests passed")
