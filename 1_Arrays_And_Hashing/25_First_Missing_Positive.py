"""
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

# Two Pointer
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        left = 0
        right = len(nums)
        while left < right:
            if nums[left] == left + 1:
                left += 1
            elif (
                nums[left] > right or
                nums[left] <= left or
                nums[nums[left] - 1] == nums[left]
            ):
                right -= 1
                nums[left], nums[right] = nums[right], nums[left]
            else:
                nums[nums[left] - 1], nums[left] = nums[left], nums[nums[left] - 1]

        return left + 1

# Array
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        idx = 0
        while idx < len(nums):
            idx_2 = nums[idx] - 1
            if nums[idx] < len(nums) and nums[idx] > 0 and nums[idx] != nums[idx_2]:
                nums[idx], nums[idx_2] = nums[idx_2], nums[idx]
            else:
                idx += 1
        for idx in range(len(nums)):
            if nums[idx] != idx + 1:
                return idx + 1
        return len(nums) + 1

# Test Cases
test_cases = [
    ([1, 2, 3, 4], 5),
    ([4, 3, 2, 1, 2], 5),
    ([_ for _ in range(-1000,1001)] + [-23], 1001),
    ([2], 1),
    ([2, 2, 2, 2, 2], 1),
    ([1,1,1,3,3,4,3,2,4,2], 5)
]

solution = Solution()
for idx, (nums, expected) in enumerate(test_cases):
    result = solution.firstMissingPositive(nums)
    print(f"Test Case {idx + 1}: {'Pass' if result == expected else 'Fail'} (Expected {expected}, Got {result})")   