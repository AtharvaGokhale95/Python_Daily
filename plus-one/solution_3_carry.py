"""
Plus One | Approach 3: Carry from the right (in place)
Topic: Math | Difficulty: Easy
https://leetcode.com/problems/plus-one/

You are given a large integer as a list `digits`, most significant digit
first, with no leading 0s. Add one to the integer and return the resulting
list of digits.

Idea: Walk from the last digit to the first. A digit below 9 gets +1 and the
method returns at once; a 9 becomes 0 and the carry moves one place left. If
every digit was 9, put a 1 in front.
Time: O(n) worst case (all 9s), O(1) when the last digit isn't 9 |
Space: O(1) extra, except the all-9s case, which builds a new list of n + 1
"""


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        """Return the digits of the number one larger than digits.

        Args:
            digits (list[int]): Digits 0-9, most significant first; must be a
                non-empty list of ints.

        Raises:
            TypeError: digits is not a list of ints.
            ValueError: digits is empty or holds a value outside 0-9.

        Returns:
            The digits of the incremented number, most significant first.
        """
        self._validate(digits)
        
        end = len(digits)                   # returns actual length: a = [1,2,3]; len(a) = 3
        for i in reversed(range(end)):      # we need to iterate on the idx, but from the last
            if digits[i] < 9:               # [1,2,3] -> for the first iteration: i = 2 -> digits[2] = 3 < 9 -> 3 + 1 = 4 -> update digits[2] = 4 and return digits = [1,2,4]
                digits[i] += 1              
                return digits               # this if loop checks only for the last digit and immediately returns the updated digits if last digit is less than 9
            else:                           # if the last digit is 9 -> a = [1,2,9] -> [1,3,0]
                digits[i] = 0
        return [1] + digits
    
    # eg 1: [1,2,3]: Last digit < 9 -> We add 1 to it -> return [1,2,4]
    # eg 2: [1,2,9]: Last digit = 9 -> we update the last index with 0 -> [1,2,0] -> for next iteraion, 2 < 9; we add 1 to it -> return [1,3,0]
    # eg 3: [9,9,9]: Last digit = 9 -> update idx = 2 with 0 -> value at idx = 1 is 9; update with 0 -> value at idx = 0 is 9; update with 0 -> exit for loop; add 1 to the list -> [1,0,0,0]

    @staticmethod
    def _validate(digits: list[int]) -> None:
        if not isinstance(digits, list):
            raise TypeError(f"digits must be a list, got {type(digits).__name__}")
        if not all(isinstance(d, int) for d in digits):
            raise TypeError("Every element in digits must be an int")
        if len(digits) == 0:
            raise ValueError("digits must not be empty")
        if not all(0 <= d <= 9 for d in digits):
            raise ValueError("Every digit must be between 0 and 9")


def short(digits) -> str:
    """Show long lists as their length so they don't flood the terminal."""
    return f"<list of {len(digits):,} digits>" if isinstance(digits, list) and len(digits) > 10 else repr(digits)


if __name__ == "__main__":
    s = Solution()

    # (digits, expected)
    cases = [
        ([1, 2, 3], [1, 2, 4]),               # basic: no carry
        ([4, 3, 2, 1], [4, 3, 2, 2]),         # LeetCode example 2
        ([0], [1]),                           # zero
        ([9], [1, 0]),                        # single 9: list grows
        ([1, 9], [2, 0]),                     # one carry
        ([1, 9, 9], [2, 0, 0]),               # carry ripples through
        ([9, 9, 9], [1, 0, 0, 0]),            # all 9s: list grows
        ([1, 0, 0], [1, 0, 1]),               # zeros stay zeros
        ([9] * 100, [1] + [0] * 100),         # large: 100 nines
    ]
    for digits, expected in cases:
        before = list(digits)                 # keep a copy to show in the output
        result = s.plusOne(digits)
        assert result == expected, f"{short(before)}: got {short(result)}, expected {short(expected)}"
        print(f"PASS digits = {short(before)} -> {short(result)}")

    # (digits, expected exception)
    bad_inputs = [
        ("123", TypeError),        # string, not a list
        ([1, "2"], TypeError),     # non-int element
        (None, TypeError),         # missing value
        ([], ValueError),          # empty list
        ([1, 10], ValueError),     # 10 is not a single digit
        ([-1], ValueError),        # negative digit
    ]
    for digits, exc in bad_inputs:
        try:
            result = s.plusOne(digits)
        except exc as e:
            print(f"PASS digits = {digits!r} -> {exc.__name__}: {e}")
        else:
            raise AssertionError(f"FAIL digits = {digits!r} -> returned {result}, expected {exc.__name__}")

    print("All tests passed")
