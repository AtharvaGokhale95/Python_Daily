"""Tests for every Longest Common Prefix solution and revisit. Run: pytest longest-common-prefix"""
import pytest

from helpers import approaches

APPROACHES = approaches(__file__, "longestCommonPrefix")

CASES = [  # (strs, expected)
    pytest.param(["flower", "flow", "flight"], "fl", id="leetcode-example-1"),
    pytest.param(["dog", "racecar", "car"], "", id="no-common-prefix"),
    pytest.param(["interspecies", "interstellar", "interstate"], "inters", id="longer-prefix"),
    pytest.param(["a"], "a", id="single-string"),
    pytest.param([""], "", id="single-empty-string"),
    pytest.param(["abc", ""], "", id="an-empty-string"),
    pytest.param(["abc", "abc", "abc"], "abc", id="all-identical"),
    pytest.param(["ab", "a"], "a", id="later-string-shorter"),
    pytest.param(["c", "acc", "ccc"], "", id="first-characters-differ"),
    pytest.param(["prefix", "pre", "preset"], "pre", id="prefix-is-a-whole-string"),
    pytest.param(["Flow", "flow"], "", id="case-sensitive"),
    pytest.param(["a" * 1000 + "x", "a" * 1000 + "y"] * 50, "a" * 1000, id="large-100-strings"),
]

BAD_INPUTS = [  # (strs, expected exception)
    pytest.param("flower", TypeError, id="string-not-list"),
    pytest.param(["a", 1], TypeError, id="non-str-element"),
    pytest.param(None, TypeError, id="none"),
    pytest.param([], ValueError, id="empty-list"),
]


@pytest.mark.parametrize("solve", APPROACHES, ids=repr)
@pytest.mark.parametrize("strs, expected", CASES)
def test_cases(solve, strs, expected):
    assert solve(list(strs)) == expected


@pytest.mark.parametrize("solve", APPROACHES, ids=repr)
@pytest.mark.parametrize("strs, exc", BAD_INPUTS)
def test_bad_inputs(solve, strs, exc):
    with pytest.raises(exc):
        solve(strs)
