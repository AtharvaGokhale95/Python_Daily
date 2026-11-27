"""
Plus One | Approach 2: Using map()
Topic: Math | Difficulty: Easy
https://leetcode.com/problems/plus-one/

You are given a large integer as a list `digits`, most significant digit
first, with no leading 0s. Add one to the integer and return the resulting
list of digits.

Idea: map(str, digits) turns each digit into a string to join into one number;
after adding 1, map(int, str(number)) splits the result back into digits.
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
        
        # map(function, iterable) applies a function to every item and returns a lazy iterator. Wrap it in list()
        integer = int("".join(map(str, digits)))            # converted the digits into into individual strings - joined them into a single string - typecasted them to int
        return list(map(int, str(integer + 1)))             # added 1 to integer - typecasted that int into string - mapped the string into int - stored in the list
        

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
