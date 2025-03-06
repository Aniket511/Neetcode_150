"""
Search in Rotated Sorted Array

Medium

There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
"""

# Solution:

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle

            if nums[left] <= nums[middle]:
                if target > nums[middle] or target < nums[left]:
                    left = middle + 1
                else:
                    right = middle - 1
                    
            else:
                if target < nums[middle] or target > nums[right]:
                    right = middle - 1
                else:
                    left = middle + 1
        return -1

test_cases = [
    ([4, 5, 6, 7, 8, 9, 1, 2, 3], 4, 0),
    ([4, 5, 6, 7, 8, 9, 1, 2, 3], 1, 6),
    ([4, 5, 6, 7, 8, 9, 1, 2, 3], 7, 3),
    ([4, 5, 6, 7, 8, 9, 1, 2, 3], 10, -1)
]

solution = Solution()

for idx, (nums, target, expected) in enumerate(test_cases):
    output = solution.search(nums, target)
    print(f"Test Case {idx + 1}: {'Pass' if output == expected else 'Fail'} (Expected {expected}, Got {output})")