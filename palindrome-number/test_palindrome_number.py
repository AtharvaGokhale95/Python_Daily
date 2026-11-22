"""Tests for every Palindrome Number solution and revisit. Run: pytest palindrome-number"""
import pytest

from helpers import approaches

APPROACHES = approaches(__file__, "isPalindrome")

CASES = [  # (x, expected)
    pytest.param(121, True, id="basic-palindrome"),
    pytest.param(-121, False, id="negative"),
    pytest.param(10, False, id="trailing-zero"),
    pytest.param(0, True, id="zero"),
    pytest.param(7, True, id="single-digit"),
    pytest.param(1221, True, id="even-digit-count"),
    pytest.param(12321, True, id="odd-digit-count"),
    pytest.param(123, False, id="not-a-palindrome"),
    pytest.param(1000021, False, id="zeros-in-the-middle"),
    pytest.param(2147447412, True, id="large-palindrome"),
]

BAD_INPUTS = [  # (x, expected exception)
    pytest.param("121", TypeError, id="string"),
    pytest.param(12.1, TypeError, id="float"),
    pytest.param(None, TypeError, id="none"),
]


@pytest.mark.parametrize("solve", APPROACHES, ids=repr)
@pytest.mark.parametrize("x, expected", CASES)
def test_cases(solve, x, expected):
    assert solve(x) is expected


@pytest.mark.parametrize("solve", APPROACHES, ids=repr)
@pytest.mark.parametrize("x, exc", BAD_INPUTS)
def test_bad_inputs(solve, x, exc):
    with pytest.raises(exc):
        solve(x)
