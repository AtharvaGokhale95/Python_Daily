"""
Day 002 - Two Sum (Arrays & Hashing)
Approach 2: One-pass hash map.

Idea: for each number, the partner it needs is (target - num).
Keep a dict of numbers already seen -> their index. If the partner
is already in the dict, we found the pair. Otherwise, store the
current number and move on.

Time: O(n)   Space: O(n)
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Return [i, j] (i < j) where nums[i] + nums[j] == target.

        Raises:
            TypeError: nums is not a list of ints, or target is not an int.
            ValueError: no two numbers add up to target.
        """
        self._validate(nums, target)

        seen: dict[int, int] = {}  # value -> index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:  # check BEFORE storing num
                return [seen[complement], i]
            seen[num] = i

        raise ValueError(f"No two numbers add up to {target}")

    @staticmethod
    def _validate(nums: list[int], target: int) -> None:
        if not isinstance(nums, list):
            raise TypeError(f"nums must be a list, got {type(nums).__name__}")
        if not all(isinstance(x, int) for x in nums):
            raise TypeError("Every element of nums must be an int")
        if not isinstance(target, int):
            raise TypeError(f"target must be an int, got {type(target).__name__}")


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
        label = f"len={len(nums)}" if len(nums) > 10 else f"{nums}"
        assert result == expected, f"{label}, {target}: got {result}, expected {expected}"

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
        except exc:
            pass
        else:
            raise AssertionError(f"Expected {exc.__name__} for {nums!r}, {target!r}")

    print("All tests passed")
