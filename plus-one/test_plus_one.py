"""Tests for every Plus One solution and revisit. Run: pytest plus-one"""
import pytest

from helpers import approaches

APPROACHES = approaches(__file__, "plusOne")

CASES = [  # (digits, expected)
    pytest.param([1, 2, 3], [1, 2, 4], id="no-carry"),
    pytest.param([4, 3, 2, 1], [4, 3, 2, 2], id="leetcode-example-2"),
    pytest.param([0], [1], id="zero"),
    pytest.param([9], [1, 0], id="single-9-list-grows"),
    pytest.param([1, 9], [2, 0], id="one-carry"),
    pytest.param([1, 9, 9], [2, 0, 0], id="carry-ripples"),
    pytest.param([9, 9, 9], [1, 0, 0, 0], id="all-9s-list-grows"),
    pytest.param([1, 0, 0], [1, 0, 1], id="zeros-stay-zeros"),
    pytest.param([9] * 100, [1] + [0] * 100, id="large-100-nines"),
]

BAD_INPUTS = [  # (digits, expected exception)
    pytest.param("123", TypeError, id="string"),
    pytest.param([1, "2"], TypeError, id="non-int-element"),
    pytest.param(None, TypeError, id="none"),
    pytest.param([], ValueError, id="empty-list"),
    pytest.param([1, 10], ValueError, id="not-a-single-digit"),
    pytest.param([-1], ValueError, id="negative-digit"),
]


@pytest.mark.parametrize("solve", APPROACHES, ids=repr)
@pytest.mark.parametrize("digits, expected", CASES)
def test_cases(solve, digits, expected):
    assert solve(list(digits)) == expected


@pytest.mark.parametrize("solve", APPROACHES, ids=repr)
@pytest.mark.parametrize("digits, exc", BAD_INPUTS)
def test_bad_inputs(solve, digits, exc):
    with pytest.raises(exc):
        solve(digits)
