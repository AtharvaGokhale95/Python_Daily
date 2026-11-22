"""
Find the Index of the First Occurrence in a String | Approach 1: Built-in method
Topic: Strings | Difficulty: Easy
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Given two strings `haystack` and `needle`, return the index of the first
occurrence of `needle` in `haystack`, or -1 if `needle` is not part of
`haystack`.
Example: haystack = "sadbutsad", needle = "sad" -> 0

Idea: str.find(needle) already returns the index of the first match, or -1
when there is none, which is exactly what the problem asks for. (str.index()
does the same search but raises ValueError instead of returning -1.)
Time: O(n + m) in practice (CPython's fast search; n = len(haystack),
m = len(needle)) | Space: O(1)
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
        
        # Both search a string for a substring and return the index of its first match. The difference is what happens when nothing is found.
        # find() returns -1
        # index() returns ValueError: substring not founc
        
        return haystack.find(needle)

    @staticmethod
    def _validate(haystack: str, needle: str) -> None:
        if not isinstance(haystack, str):
            raise TypeError(f"haystack must be a str, got {type(haystack).__name__}")
        if not isinstance(needle, str):
            raise TypeError(f"needle must be a str, got {type(needle).__name__}")
        if not haystack or not needle:
            raise ValueError("haystack and needle must not be empty")
