"""
Longest Common Prefix | Approach 1: Nested loops (character by character)
Topic: Strings | Difficulty: Easy
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst a list of
strings. If there is no common prefix, return an empty string "".

Idea: TODO (outer loop over the character positions of the first string; inner loop over the other strings; stop at the first position where a string is too short or has a different character)
Time: O(?) | Space: O(?)
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
        # TODO: write your solution here
        raise NotImplementedError

    @staticmethod
    def _validate(strs: list[str]) -> None:
        if not isinstance(strs, list):
            raise TypeError(f"strs must be a list, got {type(strs).__name__}")
        if not all(isinstance(s, str) for s in strs):
            raise TypeError("Every element in strs must be a str")
        if len(strs) == 0:
            raise ValueError("strs must not be empty")


def short(value) -> str:
    """Show long lists and strings by their size so they don't flood the terminal."""
    text = repr(value)
    if len(text) <= 60:
        return text
    if isinstance(value, list):
        return f"<list of {len(value):,} strings>"
    return f"<str of {len(value):,} chars>"


if __name__ == "__main__":
    s = Solution()

    # (strs, expected)
    cases = [
        (["flower", "flow", "flight"], "fl"),                 # LeetCode example 1
        (["dog", "racecar", "car"], ""),                      # LeetCode example 2: no common prefix
        (["interspecies", "interstellar", "interstate"], "inters"),  # longer prefix
        (["a"], "a"),                                         # single string: the prefix is the whole string
        ([""], ""),                                           # single empty string
        (["abc", ""], ""),                                    # an empty string means no prefix
        (["abc", "abc", "abc"], "abc"),                       # all identical
        (["ab", "a"], "a"),                                   # a later string is shorter than the first
        (["c", "acc", "ccc"], ""),                            # first characters differ
        (["prefix", "pre", "preset"], "pre"),                 # prefix is a whole string
        (["Flow", "flow"], ""),                               # case-sensitive
        (["a" * 1000 + "x", "a" * 1000 + "y"] * 50, "a" * 1000),  # large: 100 strings of 1,001 chars
    ]
    for strs, expected in cases:
        result = s.longestCommonPrefix(strs)
        assert result == expected, f"{short(strs)}: got {short(result)}, expected {short(expected)}"
        print(f"PASS strs = {short(strs)} -> {short(result)}")

    # (strs, expected exception)
    bad_inputs = [
        ("flower", TypeError),     # string, not a list
        (["a", 1], TypeError),     # non-str element
        (None, TypeError),         # missing value
        ([], ValueError),          # empty list
    ]
    for strs, exc in bad_inputs:
        try:
            result = s.longestCommonPrefix(strs)
        except exc as e:
            print(f"PASS strs = {strs!r} -> {exc.__name__}: {e}")
        else:
            raise AssertionError(f"FAIL strs = {strs!r} -> returned {result!r}, expected {exc.__name__}")

    print("All tests passed")
