"""
Remove Duplicates from Sorted Array | Approach 2: Two pointers (in place, sorted)
Topic: Two Pointers | Difficulty: Easy
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given an integer list `nums` sorted in non-decreasing order, remove the
duplicates so each unique value appears once, keeping their relative order.
Do it in place with O(1) extra space and return k, the number of unique
values; the first k slots of `nums` must hold them.

Idea: TODO (a write pointer k marks where the next unique value goes; a read pointer scans ahead and copies each new value to nums[k])
Time: O(?) | Space: O(?)
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
        # TODO: write your solution here
        raise NotImplementedError

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
    ]
    for nums, expected in cases:
        before = list(nums)                 # keep a copy to show in the output
        k = s.removeDuplicates(nums)        # changes nums in place
        assert k == len(expected) and nums[:k] == expected, \
            f"{before!r}: got k={k}, nums[:k]={nums[:k]}, expected {expected}"
        print(f"PASS nums = {before!r} -> k = {k}, nums[:k] = {nums[:k]}")

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
