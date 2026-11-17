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


if __name__ == "__main__":
    s = Solution()

    # (nums, expected)
    cases = [
        ([1, 1, 2], [1, 2]),                                # basic
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]),  # LeetCode example 2
        ([], []),                                           # empty list
        ([5], [5]),                                         # single element
        ([1, 2, 3], [1, 2, 3]),                             # no duplicates
        ([2, 2, 2, 2], [2]),                                # all the same
        ([-3, -3, -1, 0, 0], [-3, -1, 0]),                  # negatives and zero
        ([1, 1, 2, 3, 3], [1, 2, 3]),                       # duplicates at both ends
        (list(range(100_000)), list(range(100_000))),       # large input, no duplicates
    ]
    for nums, expected in cases:
        before = list(nums)
        result = s.removeDuplicates(nums)
        assert result == expected, f"{before!r}: got {result}, expected {expected}"
        assert nums == before, f"nums was changed: {nums!r}"                                # not in place: input must be untouched
        print(f"PASS nums = {before!r} -> {result}" if len(before) <= 10 else f"PASS nums = <list of {len(before):,} ints> -> {len(result):,} unique")

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
