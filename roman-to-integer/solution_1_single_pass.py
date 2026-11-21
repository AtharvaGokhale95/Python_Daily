"""
Roman to Integer | Approach 1: Single pass with a value map
Topic: Math | Difficulty: Easy
https://leetcode.com/problems/roman-to-integer/

Roman numerals use seven symbols: I = 1, V = 5, X = 10, L = 50, C = 100,
D = 500, M = 1000. Symbols are usually written largest to smallest, left to
right; a smaller symbol placed before a larger one is subtracted instead
(IV = 4, IX = 9, XL = 40, XC = 90, CD = 400, CM = 900). Given a Roman numeral
`s`, convert it to an integer.

Idea: Map each symbol to its value in a dict. Walk the string from right to
left: if a symbol is at least as large as the one to its right, add it;
otherwise subtract it (the I in IV, the X in XC, ...).
Time: O(n) | Space: O(1) (the 7-entry dict is fixed size)
"""


class Solution:
    # dictionary with roman number as keys and decimal integer as value
    dict ={
                'I' : 1, 
                'V' : 5, 
                'X' : 10, 
                'L' : 50, 
                'C' : 100,
                'D' : 500, 
                'M' : 1000
            }
    def romanToInt(self, s: str) -> int:
        """Return the integer value of the Roman numeral s.

        Args:
            s (str): Roman numeral; must be a non-empty string of the symbols
                I, V, X, L, C, D, M (uppercase).

        Raises:
            TypeError: s is not a string.
            ValueError: s is empty or contains a character that isn't a Roman symbol.

        Returns:
            The value of s as an int.
        """
        self._validate(s)
        
        # we will be traversing string s in reverse direction 
        previous = 0
        total = 0
        for char in reversed(s):
            current = self.dict[char]
            # traversing in reverse direction, if current > previous (VI -> V > I); then simply add current to total
            if current >= previous:
                total += current
            else:
                total -= current
            previous = current         # previous_value is updated only after if - else is completed
        return total
            

    @staticmethod
    def _validate(s: str) -> None:
        if not isinstance(s, str):
            raise TypeError(f"s must be a str, got {type(s).__name__}")
        if len(s) == 0:
            raise ValueError("s must not be empty")
        if not all(ch in "IVXLCDM" for ch in s):
            raise ValueError(f"s may only contain I, V, X, L, C, D, M, got {s!r}")


if __name__ == "__main__":
    s = Solution()

    # (numeral, expected)
    cases = [
        ("III", 3),             # LeetCode example 1: add only
        ("LVIII", 58),          # LeetCode example 2: L + V + III
        ("MCMXCIV", 1994),      # LeetCode example 3: M + CM + XC + IV
        ("I", 1),               # single symbol
        ("IV", 4),              # subtract: I before V
        ("IX", 9),              # subtract: I before X
        ("XL", 40),             # subtract: X before L
        ("XC", 90),             # subtract: X before C
        ("CD", 400),            # subtract: C before D
        ("CM", 900),            # subtract: C before M
        ("XLII", 42),           # subtraction at the start
        ("CDXLIV", 444),        # three subtractions in a row
        ("MMMCMXCIX", 3999),    # largest standard numeral
    ]
    for numeral, expected in cases:
        result = s.romanToInt(numeral)
        assert result == expected, f"{numeral!r}: got {result}, expected {expected}"
        print(f"PASS s = {numeral!r} -> {result}")

    # (numeral, expected exception)
    bad_inputs = [
        (123, TypeError),       # int, not a string
        (None, TypeError),      # missing value
        ("", ValueError),       # empty string
        ("ABC", ValueError),    # not Roman symbols
        ("iv", ValueError),     # lowercase isn't allowed
    ]
    for numeral, exc in bad_inputs:
        try:
            result = s.romanToInt(numeral)
        except exc as e:
            print(f"PASS s = {numeral!r} -> {exc.__name__}: {e}")
        else:
            raise AssertionError(f"FAIL s = {numeral!r} -> returned {result}, expected {exc.__name__}")

    print("All tests passed")
