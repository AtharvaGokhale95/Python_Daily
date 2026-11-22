"""
Palindrome Number | Approach 2: Two pointers
Topic: Math | Difficulty: Easy
https://leetcode.com/problems/palindrome-number/

Given an integer `x`, return True if `x` is a palindrome, and False
otherwise. A palindrome reads the same forwards and backwards
(121 is a palindrome; -121 and 10 are not).

Idea: Convert x to a string; with a while loop, move a left pointer
forward and a right pointer backward, comparing characters until they meet
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
        
        if len(x_str) == 1:
            return True
        
        head = 0
        tail = len(x_str) - 1
        while head < tail:
            if x_str[head] != x_str[tail]:
                return False
            head += 1
            tail -= 1
        return True
            

    @staticmethod
    def _validate(x: int) -> None:
        if not isinstance(x, int):
            raise TypeError(f"x must be an int, got {type(x).__name__}")
