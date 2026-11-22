"""
Longest Common Prefix | Approach 2: Shrink with startswith()
Topic: Strings | Difficulty: Easy
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst a list of
strings. If there is no common prefix, return an empty string "".

Idea: Start with prefix = strs[0]. For each other string, while it doesn't
start with prefix, drop the last character of prefix. Whatever survives every
string is the longest common prefix.
Time: O(n * L) checks plus up to L shrinks; worst case O(L^2) when strs[0]
(length L) is much longer than the answer, since every shrink copies the
prefix | Space: O(L) for the prefix
"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """Return the longest prefix shared by every string in strs.

        Args:
            strs (list[str]): Strings to compare; must be a non-empty list of
                strings (the strings themselves may be empty).

        Raises:
            TypeError: strs is not a list of strings.
            ValueError: strs is empty.

        Returns:
            The longest common prefix, or "" if there is none.
        """
        self._validate(strs)
        
        if not strs:
            return ""
        
        prefix = strs[0]                                # we start with assuming that the longest common prefix is the entire string at idx = 0
        
        for string in strs[1:]:                         # loop over the strings in strs starting from the second string
            while not string.startswith(prefix):
                # keep shrinking the prefix by dropping one character from the end until each string in strs starts with prefix
                prefix = prefix[:-1]
        return prefix
            

    @staticmethod
    def _validate(strs: list[str]) -> None:
        if not isinstance(strs, list):
            raise TypeError(f"strs must be a list, got {type(strs).__name__}")
        if not all(isinstance(s, str) for s in strs):
            raise TypeError("Every element in strs must be a str")
        if len(strs) == 0:
            raise ValueError("strs must not be empty")
