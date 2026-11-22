"""Tests for every Roman to Integer solution and revisit. Run: pytest roman-to-integer"""
import pytest

from helpers import approaches

APPROACHES = approaches(__file__, "romanToInt")

CASES = [  # (numeral, expected)
    pytest.param("III", 3, id="add-only"),
    pytest.param("LVIII", 58, id="leetcode-example-2"),
    pytest.param("MCMXCIV", 1994, id="leetcode-example-3"),
    pytest.param("I", 1, id="single-symbol"),
    pytest.param("IV", 4, id="IV"),
    pytest.param("IX", 9, id="IX"),
    pytest.param("XL", 40, id="XL"),
    pytest.param("XC", 90, id="XC"),
    pytest.param("CD", 400, id="CD"),
    pytest.param("CM", 900, id="CM"),
    pytest.param("XLII", 42, id="subtraction-at-the-start"),
    pytest.param("CDXLIV", 444, id="three-subtractions"),
    pytest.param("MMMCMXCIX", 3999, id="largest-numeral"),
]

BAD_INPUTS = [  # (numeral, expected exception)
    pytest.param(123, TypeError, id="int"),
    pytest.param(None, TypeError, id="none"),
    pytest.param("", ValueError, id="empty-string"),
    pytest.param("ABC", ValueError, id="not-roman-symbols"),
    pytest.param("iv", ValueError, id="lowercase"),
]


def to_roman(n: int) -> str:
    """Reference converter used to check every value from 1 to 3999."""
    out = ""
    for value, symbol in [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
                          (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]:
        while n >= value:
            out += symbol
            n -= value
    return out


@pytest.mark.parametrize("solve", APPROACHES, ids=repr)
@pytest.mark.parametrize("numeral, expected", CASES)
def test_cases(solve, numeral, expected):
    assert solve(numeral) == expected


@pytest.mark.parametrize("solve", APPROACHES, ids=repr)
def test_every_numeral_1_to_3999(solve):
    for n in range(1, 4000):
        assert solve(to_roman(n)) == n, to_roman(n)


@pytest.mark.parametrize("solve", APPROACHES, ids=repr)
@pytest.mark.parametrize("numeral, exc", BAD_INPUTS)
def test_bad_inputs(solve, numeral, exc):
    with pytest.raises(exc):
        solve(numeral)
