"""
Remove Duplicates from Sorted Array | Revisit 1 of 3 (due 2026-11-24)
Topic: Two Pointers | Difficulty: Easy
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given an integer list `nums` sorted in non-decreasing order, remove the
duplicates so each unique value appears once, keeping their relative order.

Re-solve EVERY approach from a blank file, without looking at earlier
solutions or notes. One method per approach; they can share `_validate`.
- new_list: return a NEW list of the unique values; leave nums unchanged.
- two_pointers: in place on sorted input; return k, unique values in nums[:k].
- in_place_unsorted: in place, input NOT necessarily sorted; keep the first
  occurrence of each value in its original order; return k.
Validation: raise TypeError when nums is not a list of ints.
Run the tests: pytest remove-duplicates-from-sorted-array -k revisit -v

Approach 1: New list                       | Time: O(n^2) | Space: O(n) | Result: needed help
Approach 2: Two pointers (in place, sorted) | Time: O(n)   | Space: O(1) | Result: needed help
Approach 3: In place, unsorted input       | Time: O(n)   | Space: O(n) | Result: needed help
Done 2026-11-24; marked "needed help" by Atharva. All 38 revisit tests pass.
"""


class Solution:
    def removeDuplicates_new_list(self, nums: list[int]) -> list[int]:
        
        self._validate(nums)
        """Approach 1: New list (nums unchanged)."""
        # assumption: nums is a sorted array
        
        # logic: check new_list if the num exists - if no: append it to new_list
        new_list = []
        
        for num in nums:
            if num not in new_list:
                new_list.append(num)
        return new_list

    def removeDuplicates_two_pointers(self, nums: list[int]) -> int:
        self._validate(nums)
        
        if not nums:
            return 0
        """Approach 2: Two pointers, in place, sorted input; returns k."""
        # assumption: nums is a sorted array
        
        # logic: use 2 pointers: read_idx and write_idx -> as nums is a sorted array the duplicate can only be the next element
        # we only need to check for: nums[i] != nums[i+1]
        # we will be updating the values in place: that means we use read_idx and write_idx
        
        # each non-empty list will have at least 1 unique element: nums[0]
        # so will start writing the next unique elements from nums[1]
        write_idx = 1
        
        for read_idx in range(1, len(nums)):
            if nums[read_idx] != nums[read_idx - 1]:        # comparing only with the element right before
                nums[write_idx] = nums[read_idx]
                write_idx += 1
        return write_idx                                    # this function returns an int: number of unique values

    def removeDuplicates_in_place_unsorted(self, nums: list[int]) -> int:
        self._validate(nums)
        """Approach 3: In place, unsorted input; returns k."""
        seen = set()                            # create an empty set
        
        write_idx = 0                           # idx to write in-place in nums
        for num in nums:
            if num not in seen:                 # only if num is not in seen:
                seen.add(num)                   # num will be added to seen
                nums[write_idx] = num           # num will be updated at write_idx in nums
                write_idx += 1                  # write_idx is incremented
        return len(nums[: write_idx])

    @staticmethod
    def _validate(nums: list[int]) -> None:
        if not isinstance(nums, list):
            raise TypeError(f"nums must be a list, got {type(nums).__name__}")
        if not all(isinstance(num, int) for num in nums):
            raise TypeError("Every element in nums must be an int")
