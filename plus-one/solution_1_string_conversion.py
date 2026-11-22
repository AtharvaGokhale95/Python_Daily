"""
Plus One | Approach 1: String conversion
Topic: Math | Difficulty: Easy
https://leetcode.com/problems/plus-one/

You are given a large integer as a list `digits`, most significant digit
first, with no leading 0s. Add one to the integer and return the resulting
list of digits.

Idea: Join the digits into a string, turn it into an int, add 1, then turn the
result back into a list of digits.
Time: O(n) | Space: O(n), n = number of digits
"""


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        """Return the digits of the number one larger than digits.

        Args:
            digits (list[int]): Digits 0-9, most significant first; must be a
                non-empty list of ints.

        Raises:
            TypeError: digits is not a list of ints.
            ValueError: digits is empty or holds a value outside 0-9.

        Returns:
            The digits of the incremented number, most significant first.
        """
        self._validate(digits)
        
        string = ""
        for digit in digits:
            string += str(digit)
        integer = int(string)
        integer_plusOne = integer + 1
        
        list = []
        for digit in str(integer_plusOne):
            list.append(int(digit))
        return list

    @staticmethod
    def _validate(digits: list[int]) -> None:
        if not isinstance(digits, list):
            raise TypeError(f"digits must be a list, got {type(digits).__name__}")
        if not all(isinstance(d, int) for d in digits):
            raise TypeError("Every element in digits must be an int")
        if len(digits) == 0:
            raise ValueError("digits must not be empty")
        if not all(0 <= d <= 9 for d in digits):
            raise ValueError("Every digit must be between 0 and 9")
