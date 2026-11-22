"""
Find the Index of the First Occurrence in a String | Approach 2: For loop
Topic: Strings | Difficulty: Easy
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Given two strings `haystack` and `needle`, return the index of the first
occurrence of `needle` in `haystack`, or -1 if `needle` is not part of
`haystack`.
Example: haystack = "sadbutsad", needle = "sad" -> 0

Idea: Try every start index i where needle could still fit (0 to n - m) and
compare the slice haystack[i:i + m] with needle; return the first i that
matches, or -1 after the loop.
Time: O((n - m + 1) * m), i.e. O(n * m) worst case | Space: O(m) for each slice
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """Return the index where needle first appears in haystack, or -1.

        Args:
            haystack (str): Text to search; must be a non-empty string.
            needle (str): Text to look for; must be a non-empty string.

        Raises:
            TypeError: haystack or needle is not a string.
            ValueError: haystack or needle is empty.

        Returns:
            The first index i where haystack[i:i + len(needle)] == needle, or -1.
        """
        self._validate(haystack, needle)
        
        # size of haystack
        n = len(haystack)
        
        # size of needle
        m = len(needle)
        
        # At each i, check whether the m characters starting at i equal needle
        for i in range(0, n - m + 1):               # the loop should run only until n - m + 1, as that is the last possible idx where the needle string can start
            # +1 as range stops before the end value
            if haystack[i : i + m] == needle:       # [i : i + m] - this ensures we check for needle at every i for next m chars
                return i
        return -1                                   # if there is not match      

    @staticmethod
    def _validate(haystack: str, needle: str) -> None:
        if not isinstance(haystack, str):
            raise TypeError(f"haystack must be a str, got {type(haystack).__name__}")
        if not isinstance(needle, str):
            raise TypeError(f"needle must be a str, got {type(needle).__name__}")
        if not haystack or not needle:
            raise ValueError("haystack and needle must not be empty")
