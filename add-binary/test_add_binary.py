"""Tests for every Add Binary solution and revisit. Run: pytest add-binary -v

YOU write this file. two-sum/test_two_sum.py shows the layout to follow.

Test plan (what to cover; you choose the exact inputs and expected values):
  Normal cases
    1. Both LeetCode examples.
    2. Zero on one side, and zero on both sides.
    3. Strings of different lengths.
    4. A carry that ripples all the way and makes the answer one bit longer.
    5. A case with no carry at all.
  Large input
    6. A ~10,000-bit input (LeetCode's limit). Compute the expected answer
       without calling your own solution.
  Bad inputs (which exception, TypeError or ValueError?)
    7. A non-string for a, and for b.
    8. An empty string.
    9. A character other than 0 / 1.
   10. Inputs that int(x, 2) would quietly ACCEPT but aren't valid binary
       strings: think about whitespace, "_" and a "0b" prefix.
  Bonus
   11. Many random pairs, checked against Python itself
       (hint: format(n, "b") turns an int into a binary string).

When you're done, Claude runs your tests against deliberately buggy versions
of Add Binary to see which bugs they catch.
"""

# pytest add-binary -v: points pytest to the add-binary folder
# pytest looks for the pytest.ini file - file is found in the repo root - this becomes the root folder - mentions the test file: test_*.py
# runs the following imports
import pytest
import random

# 
from helpers import approaches

# approaches(test_file, method_name)
APPROACHES = approaches(__file__, "addBinary")

cases = [ # (a, b, expected)
  pytest.param("11", "1", "100", id="leetcode-example-1"),
  pytest.param("1010", "1011", "10101", id="leetcode-example-2"),
  pytest.param("0", "0", "0", id="zero-plus-zero"),
  pytest.param("1", "0", "1", id="plus-zero"),
  pytest.param("0", "1", "1", id="zero-plus"),
  pytest.param("1", "111", "1000", id="different-lengths-carry-out"),
  pytest.param("1111", "1111", "11110", id="carry-every-step"),
  pytest.param("100", "110010", "110110", id="no-carry-different-lengths"),
  pytest.param("1" * 10_000, "1", "1" + "0" * 10_000, id="large-10000-bits")
]

bad_inputs = [
  pytest.param(11, "1", TypeError, id="a-not-str"),
  pytest.param("1", None, TypeError, id="b-not-str"),
  pytest.param("", "1", ValueError, id="empty-a"),
  pytest.param("1", "", ValueError, id="empty-b"),
  pytest.param("12", "1", ValueError, id="digit-2"),
  pytest.param("1", "1a", ValueError, id="letter"),
  pytest.param(" 1", "1", ValueError, id="space-int-would-accept"),
  pytest.param("1_0", "1", ValueError, id="underscore-int-would-accept"),
  pytest.param("0b1", "1", ValueError, id="0b-prefix")
]

@pytest.mark.parametrize("solve", APPROACHES, ids=repr)
@pytest.mark.parametrize("a, b, expected", cases)
def test_cases(solve, a, b, expected):
    assert solve(a, b) == expected


@pytest.mark.parametrize("solve", APPROACHES, ids=repr)
def test_random_against_python(solve):
    rng = random.Random(28)
    for _ in range(2_000):
        x, y = rng.randrange(1_000_000), rng.randrange(1_000_000)
        assert solve(f"{x:b}", f"{y:b}") == f"{x + y:b}", (x, y)


@pytest.mark.parametrize("solve", APPROACHES, ids=repr)
@pytest.mark.parametrize("a, b, exc", bad_inputs)
def test_bad_inputs(solve, a, b, exc):
    with pytest.raises(exc):
        solve(a, b)