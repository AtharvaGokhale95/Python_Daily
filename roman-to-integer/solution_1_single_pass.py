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
