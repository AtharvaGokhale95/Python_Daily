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
