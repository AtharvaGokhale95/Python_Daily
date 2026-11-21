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

Approach 1: Brute force       | Time: O(?) | Space: O(?) | Result: TODO
Approach 2: Hash map          | Time: O(?) | Space: O(?) | Result: TODO
"""


class Solution:
    def twoSum_brute_force(self, nums: list[int], target: int) -> list[int]:
        """Approach 1: Brute force."""
        # TODO: write your solution here
        raise NotImplementedError

    def twoSum_hash_map(self, nums: list[int], target: int) -> list[int]:
        """Approach 2: Hash map (one pass)."""
        # TODO: write your solution here
        raise NotImplementedError

    @staticmethod
    def _validate(nums: list[int], target: int) -> None:
        # TODO: raise TypeError for bad input types
        pass


def short(nums) -> str:
    """Show long lists as their length so they don't flood the terminal."""
    return f"<list of {len(nums):,} ints>" if isinstance(nums, list) and len(nums) > 10 else repr(nums)


if __name__ == "__main__":
    s = Solution()

    # (label, method, run the large-input case?)
    # Brute force is O(n^2), so it skips the 100,000-element case.
    approaches = [
        ("Approach 1: Brute force", s.twoSum_brute_force, False),
        ("Approach 2: Hash map", s.twoSum_hash_map, True),
    ]

    # (nums, target, expected)
    cases = [
        ([2, 7, 11, 15], 9, [0, 1]),           # basic
        ([3, 2, 4], 6, [1, 2]),                # can't reuse index 0 (3+3)
        ([3, 3], 6, [0, 1]),                   # duplicates
        ([-1, -2, -3, -4, -5], -8, [2, 4]),    # negatives
        ([0, 4, 3, 0], 0, [0, 3]),             # zeros
        ([5, 1, 9, 4], 13, [2, 3]),            # answer at the very end
        ([-3, 4, 3, 90], 0, [0, 2]),           # negative + positive
    ]
    large_cases = [
        (list(range(100_000)), 199_997, [99_998, 99_999]),  # large input
    ]

    # (nums, target, expected exception)
    bad_inputs = [
        ([1, 2, 3], 100, ValueError),  # no solution
        ([], 0, ValueError),           # empty list
        ([5], 10, ValueError),         # single element can't pair with itself
        ("123", 3, TypeError),         # not a list
        ([1, "2"], 3, TypeError),      # non-int element
        ([1, 2], "3", TypeError),      # non-int target
    ]

    for label, method, run_large in approaches:
        print(f"--- {label} ---")
        for nums, target, expected in cases + (large_cases if run_large else []):
            result = method(nums, target)
            assert result == expected, f"{label} | {short(nums)}, {target}: got {result}, expected {expected}"
            print(f"PASS nums = {short(nums)}, target = {target!r} -> {result}")

        for nums, target, exc in bad_inputs:
            try:
                result = method(nums, target)
            except exc as e:
                print(f"PASS nums = {nums!r}, target = {target!r} -> {exc.__name__}: {e}")
            else:
                raise AssertionError(f"FAIL {label} | nums={nums!r}, target={target!r} -> returned {result}, expected {exc.__name__}")

    print("All tests passed")
