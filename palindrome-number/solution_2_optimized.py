"""
Palindrome Number | Approach 2: Optimized (reverse half the number)
Topic: Math | Difficulty: Easy
https://leetcode.com/problems/palindrome-number/

Given an integer `x`, return True if `x` is a palindrome, and False
otherwise. A palindrome reads the same forwards and backwards
(121 is a palindrome; -121 and 10 are not).

Idea: TODO (without converting to a string: reverse the last half of the digits with % and // and compare it with the first half)
Time: O(?) | Space: O(?)
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """Return True if x reads the same forwards and backwards.

        Args:
            x (int): Value to check; must be an int.

        Raises:
            TypeError: x is not an int.

        Returns:
            True if x is a palindrome, otherwise False.
        """
        self._validate(x)
        # TODO: write your solution here
        raise NotImplementedError

    @staticmethod
    def _validate(x: int) -> None:
        if not isinstance(x, int):
            raise TypeError(f"x must be an int, got {type(x).__name__}")


if __name__ == "__main__":
    s = Solution()

    # (x, expected)
    cases = [
        (121, True),          # basic palindrome
        (-121, False),        # negative: "-121" reversed is "121-"
        (10, False),          # trailing zero: "10" reversed is "01"
        (0, True),            # single digit zero
        (7, True),            # single digit
        (1221, True),         # even number of digits
        (12321, True),        # odd number of digits
        (123, False),         # not a palindrome
        (1000021, False),     # zeros in the middle
        (2147447412, True),   # large palindrome
    ]
    for x, expected in cases:
        result = s.isPalindrome(x)
        assert result == expected, f"{x!r}: got {result}, expected {expected}"
        print(f"PASS x = {x!r} -> {result}")

    # (x, expected exception)
    bad_inputs = [
        ("121", TypeError),   # string, not int
        (12.1, TypeError),    # float, not int
        (None, TypeError),    # missing value
    ]
    for x, exc in bad_inputs:
        try:
            result = s.isPalindrome(x)
        except exc as e:
            print(f"PASS x = {x!r} -> {exc.__name__}: {e}")
        else:
            raise AssertionError(f"FAIL x = {x!r} -> returned {result}, expected {exc.__name__}")

    print("All tests passed")
