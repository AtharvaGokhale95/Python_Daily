"""
Plus One | Revisit 1 of 3 (due 2026-11-25)
Topic: Math | Difficulty: Easy
https://leetcode.com/problems/plus-one/

You are given a large integer as a list `digits`, most significant digit
first, with no leading 0s. Add one to the integer and return the resulting
list of digits.

Re-solve EVERY approach from a blank file, without looking at earlier
solutions or notes. One method per approach; they can share `_validate`.
- string_conversion: join the digits into a string, add 1, split back into digits.
- map: the same idea using map() instead of explicit loops.
- carry: walk from the right with a carry, in place.
Validation: raise TypeError when digits is not a list of ints; raise
ValueError when it is empty or holds a value outside 0-9.
Run the tests: pytest plus-one -k revisit -v

Approach 1: String conversion | Time: O(?) | Space: O(?) | Result: TODO
Approach 2: Using map()       | Time: O(?) | Space: O(?) | Result: TODO
Approach 3: Carry from right  | Time: O(?) | Space: O(?) | Result: TODO
Fill in the results (clean / needed help) when you are done.
"""


class Solution:
    def plusOne_string_conversion(self, digits: list[int]) -> list[int]:
        """Approach 1: String conversion."""
        # TODO: write your solution here
        raise NotImplementedError

    def plusOne_map(self, digits: list[int]) -> list[int]:
        """Approach 2: Using map()."""
        # TODO: write your solution here
        raise NotImplementedError

    def plusOne_carry(self, digits: list[int]) -> list[int]:
        """Approach 3: Carry from the right (in place)."""
        # TODO: write your solution here
        raise NotImplementedError

    @staticmethod
    def _validate(digits: list[int]) -> None:
        # TODO: write the validation here, then call self._validate(digits) first in each method
        raise NotImplementedError
