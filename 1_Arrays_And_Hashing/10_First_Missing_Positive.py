"""
Facebook

First Missing Positive

Hard

Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
"""

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        # Step 1: Filter out non-positive numbers since non-positive numbers are irrelevant to us for this question
        nums = [number for number in nums if number > 0]
        # Step 2: Mark the presence of NUmbers
        for number in nums:
            idx = abs(number) - 1
            if idx < len(nums) and nums[idx] > 0:
                nums[idx] *= -1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        
        return len(nums) + 1

test_cases = [
    ([1, 2, 3, 4], 5),
    ([4, 3, 2, 1, 2], 5),
    ([_ for _ in range(-100,101)] + [-23], 101),
    ([2], 1),
    ([2, 2, 2, 2, 2], 1),
    ([1,1,1,3,3,4,3,2,4,2], 5)
]

solution = Solution()
for i, (nums, expected) in enumerate(test_cases):
    result = solution.firstMissingPositive(nums)
    print(f"Test Case {i + 1}: {'Pass' if result == expected else 'Fail'} (Expected {expected}, Got {result})")