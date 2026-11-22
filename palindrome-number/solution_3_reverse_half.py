"""
Palindrome Number | Approach 3: Reverse half the number
Topic: Math | Difficulty: Easy
https://leetcode.com/problems/palindrome-number/

Given an integer `x`, return True if `x` is a palindrome, and False
otherwise. A palindrome reads the same forwards and backwards
(121 is a palindrome; -121 and 10 are not).

Idea: Without converting to a string: reverse the last half of the
digits with % and // and compare it with the first half)
Time: O(d) | Space: O(1), where d = number of digits (about log10(x))
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
        
        # // : floor division (divide, then round down) - Drops the last digit: 1234 // 10 = 123
        # % : modulo (the remainder) - Gives the last digit: 1234 % 10 = 4
        
        # negative number is never a palindrome
        # number ending in 0 is never a palindrome
        if (x < 0) or (x % 10 == 0 and x != 0):
            return False
        
        reverse = 0
        while x > reverse:
            last_digit = x % 10                         # gets the last digit for current x
            reverse = reverse * 10 + last_digit         # appends the last digit to the end
            x = x // 10                                 # drops the last digit from current x - this is the last step in the loop after the last digit is added to reverse
        
        # Even number of digits: the halves match exactly (1221 -> 12 and 12).
        # Odd number of digits: rev ends with the middle digit (12321 -> 12 and 123), so rev // 10 drops it before comparing.
        return x == reverse or x == reverse // 10
        
        
            

    @staticmethod
    def _validate(x: int) -> None:
        if not isinstance(x, int):
            raise TypeError(f"x must be an int, got {type(x).__name__}")
