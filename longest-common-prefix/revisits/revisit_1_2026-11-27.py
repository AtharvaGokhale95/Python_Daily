"""
Longest Common Prefix | Revisit 1 of 3 (due 2026-11-27)
Topic: Strings | Difficulty: Easy
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst a list of
strings. If there is no common prefix, return an empty string "".

Re-solve EVERY approach from a blank file, without looking at earlier
solutions or notes. One method per approach; they can share `_validate`.
- nested_loops: outer loop over the characters of the first string, inner loop
  over the other strings; stop at the first mismatch.
- startswith: start with the first string as the prefix and shrink it until
  every string starts with it.
Validation: raise TypeError when strs is not a list of strings; raise
ValueError when strs is empty (the strings themselves may be empty).
Run the tests: pytest longest-common-prefix -k revisit -v

Approach 1: Nested loops        | Time: O(?) | Space: O(?) | Result: TODO
Approach 2: Shrink with startswith() | Time: O(?) | Space: O(?) | Result: TODO
Fill in the results (clean / needed help) when you are done.
"""


class Solution:
    def longestCommonPrefix_nested_loops(self, strs: list[str]) -> str:
        """Approach 1: Nested loops (character by character)."""
        # TODO: write your solution here
        raise NotImplementedError

    def longestCommonPrefix_startswith(self, strs: list[str]) -> str:
        """Approach 2: Shrink with startswith()."""
        # TODO: write your solution here
        raise NotImplementedError

    @staticmethod
    def _validate(strs: list[str]) -> None:
        # TODO: write the validation here, then call self._validate(strs) first in each method
        raise NotImplementedError
