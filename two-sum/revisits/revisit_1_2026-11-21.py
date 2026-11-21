"""
Two Sum | Revisit 1 of 3 (due 2026-11-21)
Topic: Arrays & Hashing | Difficulty: Easy
https://leetcode.com/problems/two-sum/

Given a list of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to `target`. Each input has exactly one
solution, and the same element may not be used twice.

Re-solve from a blank file, without looking at earlier solutions or notes.
Validation: raise TypeError for a non-list / non-int input, ValueError when
no pair exists.

Approach used: TODO
Time: O(?) | Space: O(?)
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # TODO: write your solution here
        raise NotImplementedError


def short(nums) -> str:
    """Show long lists as their length so they don't flood the terminal."""
    return f"<list of {len(nums):,} ints>" if isinstance(nums, list) and len(nums) > 10 else repr(nums)


if __name__ == "__main__":
    s = Solution()

    # (nums, target, expected)
    cases = [
        ([2, 7, 11, 15], 9, [0, 1]),           # basic
        ([3, 2, 4], 6, [1, 2]),                # can't reuse index 0 (3+3)
        ([3, 3], 6, [0, 1]),                   # duplicates
        ([-1, -2, -3, -4, -5], -8, [2, 4]),    # negatives
        ([0, 4, 3, 0], 0, [0, 3]),             # zeros
        ([5, 1, 9, 4], 13, [2, 3]),            # answer at the very end
        ([-3, 4, 3, 90], 0, [0, 2]),           # negative + positive
        (list(range(100_000)), 199_997, [99_998, 99_999]),  # large input
    ]
    for nums, target, expected in cases:
        result = s.twoSum(nums, target)
        assert result == expected, f"{nums}, {target}: got {result}, expected {expected}"
        print(f"PASS nums = {short(nums)}, target = {target!r} -> {result}") 

    # (nums, target, expected exception)
    bad_inputs = [
        ([1, 2, 3], 100, ValueError),  # no solution
        ([], 0, ValueError),           # empty list
        ([5], 10, ValueError),         # single element can't pair with itself
        ("123", 3, TypeError),         # not a list
        ([1, "2"], 3, TypeError),      # non-int element
        ([1, 2], "3", TypeError),      # non-int target
    ]
    for nums, target, exc in bad_inputs:
        try:
            s.twoSum(nums, target)
        except exc as e:
            print(f"PASS nums = {nums!r}, target = {target!r} -> {exc.__name__}: {e}")
        else:
            raise AssertionError(f"FAIL nums={nums!r}, target={target!r} -> returned {result}, expected {exc.__name__}")

    print("All tests passed")
