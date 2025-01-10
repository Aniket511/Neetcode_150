"""
Amazon 

Single Number

Easy

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime 'O(n)' complexity and use only constant extra space 'O(1)'.

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
            result ^= number 

        # Step 4: Return the result
        # After completing the loop, 'result' will contain the unique number.
        return result

# Time Complexity:
# O(n), where n is the number of elements in the list `nums`.
# We iterate through the list once, and each XOR operation takes constant O(1) time.

# Space Complexity:
# O(1), as we use only a constant amount of extra space (the variable `result`).

# Test Cases:
test_cases = [
    ([1, 3, 7, 15, 31, 63, 63, 127, 127, 3, 1, 7, 15], 31),
    ([4, 1, 2, 1, 2], 4),
    ([-1, -1, -2], -2),
    ([1, 2, 3, 2, 3, 4, 4], 1),
    ([100], 100),
    ([_ for _ in range(-10000, 0)], 0)
]

solution = Solution()
for i, (nums, expected) in enumerate(test_cases):
    result = solution.singleNumber(nums)
    print(f"Test Case {i + 1}: {'Pass' if result == expected else 'Fail'} (Expected {expected}, Got {result})")