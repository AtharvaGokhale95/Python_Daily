"""
Palindrome Number | Revisit 1 of 3 (due 2026-11-23)
Topic: Math | Difficulty: Easy
https://leetcode.com/problems/palindrome-number/

Given an integer `x`, return True if `x` is a palindrome, and False
otherwise. A palindrome reads the same forwards and backwards
(121 is a palindrome; -121 and 10 are not).

Re-solve EVERY approach from a blank file, without looking at earlier
solutions or notes. One method per approach; they can share `_validate`.
Validation: raise TypeError when x is not an int.
Run the tests: pytest palindrome-number -k revisit -v

Approach 1: String reversal          | Time: O(d) | Space: O(d) | Result: needed help
Approach 2: Two pointers             | Time: O(d) | Space: O(d) | Result: needed help
Approach 3: Reverse half the number  | Time: O(d) | Space: O(1) | Result: needed help
d = number of digits. Done 2026-11-23 (submitted 11-24, logged on the due date at
Atharva's request); marked "needed help" by Atharva. All tests pass.
"""


class Solution:
    def isPalindrome_string_reversal(self, x: int) -> bool:
        
        self._validate(x)
        
        """Approach 1: String reversal."""
        x_rev = str(x)[::-1]
        return str(x) == x_rev

    def isPalindrome_two_pointers(self, x: int) -> bool:
        
        self._validate(x)
        
        """Approach 2: Two pointers."""
        
        # before converting x to string; check if x < 0 or x % 10 = 0 and x != 0
        if (x < 0) or (x % 10 == 0 and x != 0):
            return False
        
        x = str(x)                          # we need to typecast x to string to support indexing
        
        # As this is a two-pointer approach: Use head and tail to confirm if its a palindrome
        head = 0                            
        tail = len(x) - 1
        
        while head < tail:
            if x[tail] != x[head]:          # check for negative condition
                return False

            # if x[tail] == x[head] then we exit if condition and move head ahead by 1 and tail behind by 1 to check for next cases
            head += 1
            tail -= 1

        # until head > tail, if x[tail] == x[head] - then it is a palindrome
        # This check applies for both: len(x) is odd or even
        return True
            
    def isPalindrome_reverse_half(self, x: int) -> bool:
        
        self._validate(x)
        
        """Approach 3: Reverse half the number (no string)."""
        
        # check if x < 0 or x % 10 = 0 and x != 0: Negative number and a number ending with 0 cannot be a palindrome
        if (x < 0) or (x % 10 == 0 and x != 0):
            return False
        
        # for this approach we are not converting x into a string
        
        
        # Use % and // to reverse the entire x and then compare - store the reversed x separately
        # %: returns the last digit
        # //: drops the last digit
        rev = 0
        
        # As x is still a int, we cannot index it: So cannot use a for loop
        # Need to use while loop - condition: reversed cannot be bigger than x for it to be a palindrome
        while x > rev:
            last_digit = x % 10
            rev = rev * 10 + last_digit                # Logic to construct the decimal number - we move the last_digit from earlier iteration to the next decimal by last_digit * 10
            x = x//10                                            # update x by dropping the last_digit
        
        # x has odd no of digits (121: rev = 1, x = 12; rev = 12, x = 1) -> rev // 10 = x
        # x had even no of digits (1221: rev = 1, x = 122; rev 12, x = 12: at this step while loop will exit as x = reversed) -> if x == reversed return True
        return x == rev or x == rev//10

    @staticmethod
    def _validate(x: int) -> None:
        if not isinstance(x, int):
            raise TypeError(f"x shoud be a integer, got {type(x).__name__}")
