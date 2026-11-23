"""
Add Binary | Approach 2: Carry from the right
Topic: Math | Difficulty: Easy
https://leetcode.com/problems/add-binary/

Given two binary strings `a` and `b`, return their sum as a binary string.
Example: a = "11", b = "1" -> "100"; a = "1010", b = "1011" -> "10101"

Idea: Pad the shorter string with leading zeros (zfill) so both have length n,
then add column by column from the right like on paper: total = bit + bit +
carry, write total % 2, carry total // 2. Append a final 1 if a carry is left,
then reverse the collected digits.
Time: O(n) where n = max(len(a), len(b)) | Space: O(n) for the padded copies and the result
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """Return the sum of the binary strings a and b, as a binary string.

        Args:
            a (str): Binary number; non-empty, only the characters 0 and 1.
            b (str): Binary number; non-empty, only the characters 0 and 1.

        Raises:
            TypeError: a or b is not a string.
            ValueError: a or b is empty or contains a character other than 0 and 1.

        Returns:
            a + b written in binary, with no leading zeros (except "0" itself).
        """
        self._validate(a, b)
        
        carry = 0
        result = []             # array to store each individual binary bit after addition
        
        # pad both the binary numbers to make both of them of same lenght with leading zeros
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        
        # We need to traverse right to left to add a and b
        for i in reversed(range(n)):
            total = int(a[i]) + int(b[i]) + carry
            
            # a[i], b[i], carry: Each of these 3 things can be 0 or 1
            # total can be 0, 1, 2, 3
            
            # Logic for digit to write: total % 2 (this returns the remainder after the division with 2)
            #   If total is odd (1 or 3): write 1
            #   If total is even (0 or 2): write 0
            result.append(str(total % 2))

            # Logic for digit to carry: total // 2 (this returns either of 0 or 1)
            # If total is > 1: (2, 3) -> carry = 1
            # If total is <= 1: (0, 1) -> carry = 0
            carry = total // 2
        
        if carry:           # if carry != 0
            result.append("1")
        
        # when we append total to result, it appended from left to right; so we need reversed
        return "".join(reversed(result))

    @staticmethod
    def _validate(a: str, b: str) -> None:
        for name, value in (("a", a), ("b", b)):
            if not isinstance(value, str):
                raise TypeError(f"{name} must be a str, got {type(value).__name__}")
            if not value:
                raise ValueError(f"{name} must not be empty")
            if not all(ch in "01" for ch in value):
                raise ValueError(f"{name} may only contain 0 and 1, got {value!r}")
