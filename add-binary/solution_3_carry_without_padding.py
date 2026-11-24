"""
Add Binary | Approach 3: Carry without padding
Topic: Math | Difficulty: Easy
https://leetcode.com/problems/add-binary/

Given two binary strings `a` and `b`, return their sum as a binary string.
Example: a = "11", b = "1" -> "100"; a = "1010", b = "1011" -> "10101"

Idea: No padding: one index per string, both starting at the last character.
Loop while either index is still >= 0 or a carry is left; each round starts
total at carry and adds a[i] / b[j] only if that string still has bits. Write
total % 2, carry total // 2; the final carry is handled inside the loop.
Collect digits, then reverse.
Time: O(max(n, m)) | Space: O(max(n, m)) for the result (no padded copies)
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
        result = []
    
        # for this solution, the string a and b are not padded - they can have different lengths: so we are using two separate pointers
        # following are the right most positions of a and b
        i = len(a) - 1      
        j = len(b) - 1
        
        # while loop joins all 3 conditions using OR - it only tells you that at least one of them is true. It doesn't tell you which. Each if checks one specific source
        while i >= 0 or j >= 0 or carry:        # is there any work left - any bits pending to add or carry to add
            
            total = carry
            
            if i >= 0:                          # if conditions checks if "a" still have a digit in the current column
                total += int(a[i])              # we separately add a[i] to total
                i -= 1
                
            if j >= 0:                          # if conditions checks if "a" still have a digit in the current column
                total += int(b[j])              # we separately add b[j] to total
                j -= 1
            
            result.append(str(total % 2))       # digit to write
            carry = total // 2                  # digit to carry
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
