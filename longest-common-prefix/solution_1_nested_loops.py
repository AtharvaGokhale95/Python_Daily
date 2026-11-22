"""
Longest Common Prefix | Approach 1: Nested loops (character by character)
Topic: Strings | Difficulty: Easy
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst a list of
strings. If there is no common prefix, return an empty string "".

Idea: Outer loop over the character positions of the first string; inner loop
over the other strings. Stop at the first position where a string is too short
or has a different character; until then, add the character to the prefix.
Time: O(S), S = total characters compared (at most n strings x m prefix chars) |
Space: O(m) for the prefix
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
        
        prefix = ""
        for i in range(len(strs[0])):       # outer loop iterates over only the first string in strs; strs[0]
            current_char = strs[0][i]       # capture one char at a time from strs[0]                 
            
            for string in strs[1:]:         # inner loop iterates from the second string in strs until the end; we will use the same idx from outer loop
                if i >= len(string) or string[i] != current_char:
                    return prefix
                # inner loop checks if we find a char which is not common so that we can return the longest common prefix 
            
            # if the control does not enter the if loop, we exit for loop and update the prefix with new character
            prefix += current_char
        
        return prefix
            

    @staticmethod
    def _validate(strs: list[str]) -> None:
        if not isinstance(strs, list):
            raise TypeError(f"strs must be a list, got {type(strs).__name__}")
        if not all(isinstance(s, str) for s in strs):
            raise TypeError("Every element in strs must be a str")
        if len(strs) == 0:
            raise ValueError("strs must not be empty")
