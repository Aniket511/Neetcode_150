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

test_cases = [
    ([2, 7, 11, 15], 9, [0, 1]),       # 2 + 7 = 9
    ([3, 2, 4], 6, [1, 2]),            # 2 + 4 = 6
    ([3, 3], 6, [0, 1]),               # 3 + 3 = 6
    ([1, 2, 3, 4, 5], 10, None),       # No valid pair
    ([0, 4, 3, 0], 0, [0, 3]),         # 0 + 0 = 0
    ([1, -1, 2, -2], 0, [1, 3])        # -1 + 1 = 0
]

solution = Solution()
for i, (nums, target, expected) in enumerate(test_cases):
    result = solution.twoSum(nums, target)
    print(f"Test Case {i+1}: {nums, result}")