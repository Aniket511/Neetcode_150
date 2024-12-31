"""
Two Sum

Easy
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order. 

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

# Solution : Hashmap
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Step 1: Initialize a hashmap to store the indices of visited numbers
        pair_idx = {}

        # Step 2: Iterate through the list with index and value
        for idx, number in enumerate(nums):
            # Calculate the difference needed to reach the target
            difference = target - number

            # Check if the difference exists in the hashmap
            if difference in pair_idx:
                # If found, return the indices sorted in ascending order
                return sorted([pair_idx[difference], idx])
            
            # Store the current number with its index in the hashmap
            pair_idx[number] = idx

# Time Complexity:
# O(n) where n is the len of nums because we iterate through all values of nums

# Space Complexity:
# O(n) where n is the length of nums

# Test Cases:
test_cases = [
    ([3, 4, 5, 6], 7),      # The correct answer for this would be indices [0, 2] as 3 + 4 = 7
    ([1, 2, 3, 4], 5),      # The correct answer for this would be indices [0, 3] as 1 + 4 = 5
    ([-1, -2, -3, -1], -5), # The correct answer for this would be indices [1, 2] as -2 + -3 = -5
]

solution = Solution()  # Corrected instantiation of Solution class
for i, (nums, target) in enumerate(test_cases):
    result = solution.twoSum(nums, target)  # Calling the method with correct arguments
    expected = sorted([nums.index(target - nums[i]), i])  # Getting the expected result
    print(f"Test Case {i + 1}: {'Pass' if result == expected else 'Fail'} (Expected {expected}, Got {result})")