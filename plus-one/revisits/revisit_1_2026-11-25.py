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

Approach 1: String conversion | Time: O(n) | Space: O(n) | Result: needed help
Approach 2: Using map()       | Time: O(n) | Space: O(n) | Result: needed help
Approach 3: Carry from right  | Time: O(n) worst, O(1) typical | Space: O(1) extra (O(n) if all 9s) | Result: needed help
n = number of digits. Done 2026-11-25 (submitted 11-26, logged on the due date at
Atharva's request); marked "needed help" by Atharva. All 15 tests pass for each method.
"""


class Solution:
    def plusOne_string_conversion(self, digits: list[int]) -> list[int]:
        self._validate(digits)
        """Approach 1: String conversion."""
        # Convert digits to string -> convert to int -> add one
        # Using for loop again create a new list for integer_plusOne
        string = ""
        for digit in digits:
            string += str(digit)
        
        integer = int(string)
        integer_plusOne = integer + 1
        
        list = []
        for digit in str(integer_plusOne):
            list.append(int(digit))
        return list

    def plusOne_map(self, digits: list[int]) -> list[int]:
        self._validate(digits)
        """Approach 2: Using map()."""
        # map(function, iterable)
        integer = int("".join(map(str, digits)))
        return list(map(int, str(integer + 1)))
        

    def plusOne_carry(self, digits: list[int]) -> list[int]:
        self._validate(digits)
        """Approach 3: Carry from the right (in place)."""
        end = len(digits)                   # returns actual length: a = [1,2,3]; len(a) = 3
        for i in reversed(range(end)):      # we need to iterate on the idx, but from the last
            if digits[i] < 9:               # [1,2,3] -> for the first iteration: i = 2 -> digits[2] = 3 < 9 -> 3 + 1 = 4 -> update digits[2] = 4 and return digits = [1,2,4]
                digits[i] += 1              
                return digits               # this if loop checks only for the last digit and immediately returns the updated digits if last digit is less than 9
            else:                           # if the last digit is 9 -> a = [1,2,9] -> [1,3,0]
                digits[i] = 0
        return [1] + digits
        

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
