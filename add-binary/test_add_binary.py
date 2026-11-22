"""Tests for every Add Binary solution and revisit. Run: pytest add-binary"""
import random

import pytest

from helpers import approaches

APPROACHES = approaches(__file__, "addBinary")

CASES = [  # (a, b, expected)
    pytest.param("11", "1", "100", id="leetcode-example-1"),
    pytest.param("1010", "1011", "10101", id="leetcode-example-2"),
    pytest.param("0", "0", "0", id="zero-plus-zero"),
    pytest.param("1", "0", "1", id="plus-zero"),
    pytest.param("0", "1", "1", id="zero-plus"),
    pytest.param("1", "111", "1000", id="different-lengths-carry-out"),
    pytest.param("1111", "1111", "11110", id="carry-every-step"),
    pytest.param("100", "110010", "110110", id="no-carry-different-lengths"),
    pytest.param("1" * 10_000, "1", "1" + "0" * 10_000, id="large-10000-bits"),
]

BAD_INPUTS = [  # (a, b, expected exception)
    pytest.param(11, "1", TypeError, id="a-not-str"),
    pytest.param("1", None, TypeError, id="b-not-str"),
    pytest.param("", "1", ValueError, id="empty-a"),
    pytest.param("1", "", ValueError, id="empty-b"),
    pytest.param("12", "1", ValueError, id="digit-2"),
    pytest.param("1", "1a", ValueError, id="letter"),
    pytest.param(" 1", "1", ValueError, id="space-int-would-accept"),
    pytest.param("1_0", "1", ValueError, id="underscore-int-would-accept"),
    pytest.param("0b1", "1", ValueError, id="0b-prefix"),
]


@pytest.mark.parametrize("solve", APPROACHES, ids=repr)
@pytest.mark.parametrize("a, b, expected", CASES)
def test_cases(solve, a, b, expected):
    assert solve(a, b) == expected


@pytest.mark.parametrize("solve", APPROACHES, ids=repr)
def test_random_against_python(solve):
    rng = random.Random(28)
    for _ in range(2_000):
        x, y = rng.randrange(1_000_000), rng.randrange(1_000_000)
        assert solve(f"{x:b}", f"{y:b}") == f"{x + y:b}", (x, y)


@pytest.mark.parametrize("solve", APPROACHES, ids=repr)
@pytest.mark.parametrize("a, b, exc", BAD_INPUTS)
def test_bad_inputs(solve, a, b, exc):
    with pytest.raises(exc):
        solve(a, b)
