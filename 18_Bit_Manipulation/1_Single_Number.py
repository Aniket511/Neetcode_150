"""
Single Number

Easy

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
"""

# Solution: Bit Manipulation
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # Step 1: Initialize a variable 'result' to 0
        # This variable will store the result, which is the number that appears only once.
        result = 0

        # Step 2: Iterate through each number in the list 'nums'
        for number in nums:
            # Step 3: XOR the current number with 'result'
            # The XOR operation cancels out numbers that appear twice.
            result = number ^ result

        # Step 4: Return the result
        # After completing the loop, 'result' will contain the unique number.
        return result

# Time Complexity:
# O(n), where n is the number of elements in the list `nums`.
# We iterate through the list once, and each XOR operation takes constant time.

# Space Complexity:
# O(1), as we use only a constant amount of extra space (the variable `result`).

# Test cases to validate the solution
# Test case 1: General case with one unique number
nums1 = [4, 1, 2, 1, 2]
solution = Solution()
print(solution.singleNumber(nums1))  # Expected output: 4

# Test case 2: Case where the single number is negative
nums2 = [-1, 2, 2, 3, 3]
print(solution.singleNumber(nums2))  # Expected output: -1

# Test case 3: Case with only one element in the list
nums3 = [5]
print(solution.singleNumber(nums3))  # Expected output: 5

# Test case 4: Case with all numbers repeated except one
nums4 = [7, 8, 8, 9, 9]
print(solution.singleNumber(nums4))  # Expected output: 7

# Test case 5: Case with all numbers repeated except one, with a larger list
nums5 = [10, 20, 10, 30, 30, 40, 40]
print(solution.singleNumber(nums5))  # Expected output: 20