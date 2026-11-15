"""
Day 1: Two Sum
Topic: Arrays & Hashing | Difficulty: Easy
https://leetcode.com/problems/two-sum/

Given a list of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to `target`. Each input has exactly one
solution, and the same element may not be used twice.
"""


# Approach 1: Brute force
def two_sum_brute_force(nums: list[int], target: int) -> list[int]:
    """Time: O(?) | Space: O(?)"""
    # TODO: write your brute-force solution here
    raise NotImplementedError


# Approach 2: Optimized
def two_sum_optimized(nums: list[int], target: int) -> list[int]:
    """Time: O(?) | Space: O(?)"""
    # TODO: write your optimized solution here
    raise NotImplementedError


if __name__ == "__main__":
    tests = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]
    for fn in (two_sum_brute_force, two_sum_optimized):
        for nums, target, expected in tests:
            try:
                result = sorted(fn(nums, target))
                status = "PASS" if result == expected else f"FAIL (got {result})"
            except NotImplementedError:
                status = "not written yet"
            print(f"{fn.__name__}({nums}, {target}) -> {status}")
