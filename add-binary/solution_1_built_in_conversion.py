"""
Add Binary | Approach 1: Built-in conversion
Topic: Math | Difficulty: Easy
https://leetcode.com/problems/add-binary/

Given two binary strings `a` and `b`, return their sum as a binary string.
Example: a = "11", b = "1" -> "100"; a = "1010", b = "1011" -> "10101"

Idea: TODO (int(text, 2) reads a binary string as a number; bin(n) turns a number back into text, but with a prefix you need to remove)
Time: O(?) | Space: O(?)
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """Return the sum of the binary strings a and b, as a binary string.

        Args:
            a (str): Binary number; non-empty, only the characters 0 and 1.
            b (str): Binary number; non-empty, only the characters 0 and 1.

        Raises:
            TypeError: a or b is not a string.
            ValueError: a or b is empty or contains a character other than 0 and 1.

        Returns:
            a + b written in binary, with no leading zeros (except "0" itself).
        """
        self._validate(a, b)
        # TODO: write your solution here
        raise NotImplementedError

    @staticmethod
    def _validate(a: str, b: str) -> None:
        for name, value in (("a", a), ("b", b)):
            if not isinstance(value, str):
                raise TypeError(f"{name} must be a str, got {type(value).__name__}")
            if not value:
                raise ValueError(f"{name} must not be empty")
            if not all(ch in "01" for ch in value):
                raise ValueError(f"{name} may only contain 0 and 1, got {value!r}")
