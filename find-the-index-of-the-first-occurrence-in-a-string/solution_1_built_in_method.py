"""
Find the Index of the First Occurrence in a String | Approach 1: Built-in method
Topic: Strings | Difficulty: Easy
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Given two strings `haystack` and `needle`, return the index of the first
occurrence of `needle` in `haystack`, or -1 if `needle` is not part of
`haystack`.
Example: haystack = "sadbutsad", needle = "sad" -> 0

Idea: TODO (a str method already does this search; check what find() returns when needle is missing, and how index() differs)
Time: O(?) | Space: O(?)
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
        # TODO: write your solution here
        raise NotImplementedError

    @staticmethod
    def _validate(haystack: str, needle: str) -> None:
        if not isinstance(haystack, str):
            raise TypeError(f"haystack must be a str, got {type(haystack).__name__}")
        if not isinstance(needle, str):
            raise TypeError(f"needle must be a str, got {type(needle).__name__}")
        if not haystack or not needle:
            raise ValueError("haystack and needle must not be empty")


def short(text) -> str:
    """Show long strings as their length so they don't flood the terminal."""
    return f"<str of {len(text):,} chars>" if isinstance(text, str) and len(text) > 30 else repr(text)


if __name__ == "__main__":
    s = Solution()

    # (haystack, needle, expected)
    cases = [
        ("sadbutsad", "sad", 0),          # LeetCode example 1: found at the start (and again later)
        ("leetcode", "leeto", -1),        # LeetCode example 2: not found
        ("hello", "ll", 2),               # found in the middle
        ("abc", "c", 2),                  # found at the very end
        ("a", "a", 0),                    # single characters
        ("abc", "abc", 0),                # needle is the whole haystack
        ("aaa", "aaaa", -1),              # needle longer than haystack
        ("mississippi", "issip", 4),      # partial match "issis" first, real match later
        ("aaaaab", "aab", 3),             # overlapping partial matches
        ("a" * 10_000 + "b", "a" * 500 + "b", 9_500),  # large input, match at the end
    ]
    for haystack, needle, expected in cases:
        result = s.strStr(haystack, needle)
        assert result == expected, f"{short(haystack)}, {short(needle)}: got {result}, expected {expected}"
        print(f"PASS haystack = {short(haystack)}, needle = {short(needle)} -> {result}")

    # (haystack, needle, expected exception)
    bad_inputs = [
        (123, "a", TypeError),            # haystack not a string
        ("abc", None, TypeError),         # needle not a string
        (["a", "b"], "a", TypeError),     # list, not a string
        ("", "a", ValueError),            # empty haystack
        ("abc", "", ValueError),          # empty needle
    ]
    for haystack, needle, exc in bad_inputs:
        try:
            result = s.strStr(haystack, needle)
        except exc as e:
            print(f"PASS haystack = {haystack!r}, needle = {needle!r} -> {exc.__name__}: {e}")
        else:
            raise AssertionError(f"FAIL haystack = {haystack!r}, needle = {needle!r} -> returned {result}, expected {exc.__name__}")

    print("All tests passed")
