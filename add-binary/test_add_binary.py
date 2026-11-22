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
import pytest

from helpers import approaches

APPROACHES = approaches(__file__, "addBinary")

# TODO: CASES = [pytest.param(a, b, expected, id="..."), ...]
# TODO: BAD_INPUTS = [...]
# TODO: test functions with @pytest.mark.parametrize("solve", APPROACHES, ids=repr)
