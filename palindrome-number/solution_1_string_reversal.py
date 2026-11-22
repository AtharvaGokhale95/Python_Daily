"""
Palindrome Number | Approach 1: String reversal
Topic: Math | Difficulty: Easy
https://leetcode.com/problems/palindrome-number/

Given an integer `x`, return True if `x` is a palindrome, and False
otherwise. A palindrome reads the same forwards and backwards
(121 is a palindrome; -121 and 10 are not).

Idea: Convert x to a string and compare it with its reverse (x_str[::-1]).
A negative number never matches, because its "-" ends up at the end.
Time: O(d) | Space: O(d), where d = number of digits (about log10(x))
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
        
        x_str = str(x)
        x_str_rev = x_str[::-1]
        return x_str == x_str_rev
        

    @staticmethod
    def _validate(x: int) -> None:
        if not isinstance(x, int):
            raise TypeError(f"x must be an int, got {type(x).__name__}")
