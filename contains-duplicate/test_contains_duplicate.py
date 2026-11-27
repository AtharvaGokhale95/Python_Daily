"""Tests for every Contains Duplicate solution and revisit. Run: pytest contains-duplicate"""
import random

import pytest

from helpers import approaches

APPROACHES = approaches(__file__, "containsDuplicate")
SLOW = {"brute_force"}  # O(n^2): skips the 100,000-element cases

CASES = [  # (nums, expected)
    pytest.param([1, 2, 3, 1], True, id="leetcode-example-1"),
    pytest.param([1, 2, 3, 4], False, id="leetcode-example-2"),
    pytest.param([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True, id="leetcode-example-3"),
    pytest.param([], False, id="empty-list"),
    pytest.param([5], False, id="single-element"),
    pytest.param([7, 7], True, id="just-a-pair"),
    pytest.param([1, 2, 3, 4, 5, 5], True, id="duplicate-at-the-end"),
    pytest.param([4, 4, 1, 2, 3], True, id="duplicate-at-the-start"),
    pytest.param([9, 1, 2, 3, 9], True, id="duplicates-far-apart"),
    pytest.param([2, 1, 2], True, id="unsorted-duplicate-not-adjacent"),
    pytest.param([-1, -2, -3, -1], True, id="negative-duplicate"),
    pytest.param([-1, 1], False, id="negative-and-positive-are-different"),
    pytest.param([0, 0], True, id="zeros"),
    pytest.param([0, 1, 2], False, id="zero-once"),
    pytest.param([10**9, -10**9, 10**9], True, id="extreme-values"),
    pytest.param([3, 1, 2, 5, 4], False, id="unsorted-all-distinct"),
]

BAD_INPUTS = [  # (nums, expected exception)
    pytest.param("1231", TypeError, id="string"),
    pytest.param(None, TypeError, id="none"),
    pytest.param((1, 2, 3), TypeError, id="tuple"),
    pytest.param({1, 2, 3}, TypeError, id="set"),
    pytest.param([1, "2"], TypeError, id="non-int-element"),
    pytest.param([1.5, 2.5], TypeError, id="floats"),
]


@pytest.mark.parametrize("solve", APPROACHES, ids=repr)
@pytest.mark.parametrize("nums, expected", CASES)
def test_cases(solve, nums, expected):
    assert solve(list(nums)) is expected


@pytest.mark.parametrize("solve", APPROACHES, ids=repr)
@pytest.mark.parametrize("nums, exc", BAD_INPUTS)
def test_bad_inputs(solve, nums, exc):
    with pytest.raises(exc):
        solve(nums)


@pytest.mark.parametrize("solve", APPROACHES, ids=repr)
@pytest.mark.parametrize("nums", [[3, 1, 2, 3], [5, 4, 3, 2, 1], [2, 2, 1, 1]])
def test_input_not_modified(solve, nums):
    before = list(nums)
    solve(nums)
    assert nums == before


@pytest.mark.parametrize("solve", APPROACHES, ids=repr)
def test_medium_input(solve):
    assert solve(list(range(1_500))) is False
    assert solve(list(range(1_500)) + [750]) is True


@pytest.mark.parametrize("solve", [a for a in APPROACHES if a.style not in SLOW], ids=repr)
def test_large_input(solve):
    assert solve(list(range(100_000))) is False
    assert solve(list(range(100_000)) + [0]) is True
    assert solve([1] * 100_000) is True


@pytest.mark.parametrize("solve", APPROACHES, ids=repr)
def test_random_against_set(solve):
    rng = random.Random(217)
    for _ in range(300):
        nums = [rng.randint(-20, 20) for _ in range(rng.randint(0, 25))]
        assert solve(list(nums)) is (len(set(nums)) != len(nums)), nums
