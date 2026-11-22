"""Tests for every Remove Duplicates from Sorted Array solution and revisit.
Run: pytest remove-duplicates-from-sorted-array

Two contracts:
- "new_list" returns a new list and must leave nums unchanged.
- every other approach works in place: returns k, with the unique values in nums[:k].
"""
import pytest

from helpers import approaches

APPROACHES = approaches(__file__, "removeDuplicates")
NEW_LIST = {"new_list"}               # returns a list instead of k
UNSORTED_OK = {"in_place_unsorted"}   # also handles unsorted input
SLOW = {"new_list"}                   # O(n^2): skips the 100,000-element case

CASES = [  # (nums, expected unique values)
    pytest.param([1, 1, 2], [1, 2], id="basic"),
    pytest.param([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4], id="leetcode-example-2"),
    pytest.param([], [], id="empty-list"),
    pytest.param([5], [5], id="single-element"),
    pytest.param([1, 2, 3], [1, 2, 3], id="no-duplicates"),
    pytest.param([2, 2, 2, 2], [2], id="all-the-same"),
    pytest.param([-3, -3, -1, 0, 0], [-3, -1, 0], id="negatives-and-zero"),
    pytest.param([1, 1, 2, 3, 3], [1, 2, 3], id="duplicates-at-both-ends"),
]

UNSORTED_CASES = [  # only for approaches in UNSORTED_OK
    pytest.param([3, 1, 3, 2, 1], [3, 1, 2], id="unsorted"),
    pytest.param([4, 4, 1, 4, 1], [4, 1], id="unsorted-repeats-far-apart"),
    pytest.param([0, -1, 0, -1, 2], [0, -1, 2], id="unsorted-with-negatives"),
]

BAD_INPUTS = [  # (nums, expected exception)
    pytest.param("112", TypeError, id="string"),
    pytest.param([1, "2"], TypeError, id="non-int-element"),
    pytest.param(None, TypeError, id="none"),
]


def check(solve, nums, expected):
    before = list(nums)
    result = solve(nums)
    if solve.style in NEW_LIST:
        assert result == expected
        assert nums == before, "not in place: the input must be unchanged"
    else:
        assert result == len(expected)
        assert nums[:result] == expected


@pytest.mark.parametrize("solve", APPROACHES, ids=repr)
@pytest.mark.parametrize("nums, expected", CASES)
def test_cases(solve, nums, expected):
    check(solve, list(nums), expected)


@pytest.mark.parametrize("solve", [a for a in APPROACHES if a.style in UNSORTED_OK], ids=repr)
@pytest.mark.parametrize("nums, expected", UNSORTED_CASES)
def test_unsorted(solve, nums, expected):
    check(solve, list(nums), expected)


@pytest.mark.parametrize("solve", [a for a in APPROACHES if a.style not in SLOW], ids=repr)
def test_large_input(solve):
    nums = [n // 2 for n in range(200_000)]   # 0, 0, 1, 1, ... 99_999, 99_999
    check(solve, nums, list(range(100_000)))


@pytest.mark.parametrize("solve", APPROACHES, ids=repr)
@pytest.mark.parametrize("nums, exc", BAD_INPUTS)
def test_bad_inputs(solve, nums, exc):
    with pytest.raises(exc):
        solve(nums)
