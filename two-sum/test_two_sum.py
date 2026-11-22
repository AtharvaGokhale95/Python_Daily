"""Tests for every Two Sum solution and revisit. Run: pytest two-sum"""
import pytest

from helpers import approaches

APPROACHES = approaches(__file__, "twoSum")
SLOW = {"brute_force"}  # O(n^2): skips the 100,000-element case

CASES = [  # (nums, target, expected)
    pytest.param([2, 7, 11, 15], 9, [0, 1], id="basic"),
    pytest.param([3, 2, 4], 6, [1, 2], id="cant-reuse-index-0"),
    pytest.param([3, 3], 6, [0, 1], id="duplicates"),
    pytest.param([-1, -2, -3, -4, -5], -8, [2, 4], id="negatives"),
    pytest.param([0, 4, 3, 0], 0, [0, 3], id="zeros"),
    pytest.param([5, 1, 9, 4], 13, [2, 3], id="answer-at-the-end"),
    pytest.param([-3, 4, 3, 90], 0, [0, 2], id="negative-plus-positive"),
    pytest.param([1, 3, 4, 2], 6, [2, 3], id="3+3-would-reuse-index-1"),
]

BAD_INPUTS = [  # (nums, target, expected exception)
    pytest.param([1, 2, 3], 100, ValueError, id="no-solution"),
    pytest.param([], 0, ValueError, id="empty-list"),
    pytest.param([5], 10, ValueError, id="single-element"),
    pytest.param("123", 3, TypeError, id="not-a-list"),
    pytest.param([1, "2"], 3, TypeError, id="non-int-element"),
    pytest.param([1, 2], "3", TypeError, id="non-int-target"),
    pytest.param([1.5, 0.5], 2, TypeError, id="floats"),
]


@pytest.mark.parametrize("solve", APPROACHES, ids=repr)
@pytest.mark.parametrize("nums, target, expected", CASES)
def test_cases(solve, nums, target, expected):
    assert solve(list(nums), target) == expected


@pytest.mark.parametrize("solve", [a for a in APPROACHES if a.style not in SLOW], ids=repr)
def test_large_input(solve):
    assert solve(list(range(100_000)), 199_997) == [99_998, 99_999]


@pytest.mark.parametrize("solve", APPROACHES, ids=repr)
@pytest.mark.parametrize("nums, target, exc", BAD_INPUTS)
def test_bad_inputs(solve, nums, target, exc):
    with pytest.raises(exc):
        solve(nums, target)
