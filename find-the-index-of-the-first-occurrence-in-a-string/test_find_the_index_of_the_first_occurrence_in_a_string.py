"""Tests for every Find the Index of the First Occurrence in a String solution and revisit.
Run: pytest find-the-index-of-the-first-occurrence-in-a-string
"""
import pytest

from helpers import approaches

APPROACHES = approaches(__file__, "strStr")

CASES = [  # (haystack, needle, expected)
    pytest.param("sadbutsad", "sad", 0, id="found-at-start"),
    pytest.param("leetcode", "leeto", -1, id="not-found"),
    pytest.param("hello", "ll", 2, id="found-in-middle"),
    pytest.param("abc", "c", 2, id="found-at-end"),
    pytest.param("a", "a", 0, id="single-characters"),
    pytest.param("abc", "abc", 0, id="needle-is-whole-haystack"),
    pytest.param("aaa", "aaaa", -1, id="needle-longer"),
    pytest.param("mississippi", "issip", 4, id="partial-match-first"),
    pytest.param("aaaaab", "aab", 3, id="overlapping-partial-matches"),
    pytest.param("a" * 10_000 + "b", "a" * 500 + "b", 9_500, id="large-match-at-end"),
]

BAD_INPUTS = [  # (haystack, needle, expected exception)
    pytest.param(123, "a", TypeError, id="haystack-not-str"),
    pytest.param("abc", None, TypeError, id="needle-not-str"),
    pytest.param(["a", "b"], "a", TypeError, id="list"),
    pytest.param("", "a", ValueError, id="empty-haystack"),
    pytest.param("abc", "", ValueError, id="empty-needle"),
]


@pytest.mark.parametrize("solve", APPROACHES, ids=repr)
@pytest.mark.parametrize("haystack, needle, expected", CASES)
def test_cases(solve, haystack, needle, expected):
    assert solve(haystack, needle) == expected


@pytest.mark.parametrize("solve", APPROACHES, ids=repr)
@pytest.mark.parametrize("haystack, needle, exc", BAD_INPUTS)
def test_bad_inputs(solve, haystack, needle, exc):
    with pytest.raises(exc):
        solve(haystack, needle)
