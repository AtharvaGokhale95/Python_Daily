"""
Day 1: Two Sum | Approach 1: Brute force
Topic: Arrays & Hashing | Difficulty: Easy
https://leetcode.com/problems/two-sum/

Given a list of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to `target`. Each input has exactly one
solution, and the same element may not be used twice.

Idea: TODO
Time: O(?) | Space: O(?)
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    # TODO: write your brute-force solution here
    raise NotImplementedError


if __name__ == "__main__":
    tests = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]
    for nums, target, expected in tests:
        result = sorted(two_sum(nums, target))
        print(f"two_sum({nums}, {target}) -> {result}", "PASS" if result == expected else f"FAIL (expected {expected})")
