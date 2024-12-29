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
        # The algorithm starts by creating a new list that only includes positive numbers from the original nums list. 
        # Non-positive numbers (i.e., zero or negative numbers) are irrelevant to finding the smallest missing positive integer and are therefore removed.
        nums = [number for number in nums if number > 0]
        # Step 2: Mark the presence of numbers
        for number in nums:
            # The algorithm calculates the index idx by taking the absolute value of 'number' and subtracting 1. This converts the value 'number' to a zero-based index
            idx = abs(number) - 1
            # If idx is within the bounds of the list (idx < len(nums)) and the value at nums[idx] is positive, 
            # the algorithm marks the presence of the number by negating the value at nums[idx]
            if idx < len(nums) and nums[idx] > 0:
                # By negating the values, the algorithm effectively marks that a number corresponding to this index exists in the array, without using extra space
                nums[idx] *= -1
        # Step 3: Identify the first missing positive
        # Iterating through the list to checks each element in the list from left to right
        for idx in range(len(nums)):
            # If an element is found to be positive, it indicates that the index i + 1 is the first missing positive integer because this index was not marked in the previous step.
            if nums[idx] > 0:
                return idx + 1
        # Step 4: Return the next positive integer
        # If the loop completes without finding a missing positive integer, it means all integers from 1 to len(nums) are present in the array. 
        # Therefore, the first missing positive integer would be len(nums) + 1
        return len(nums) + 1

# Time Complexity:
# The time complexity of the provided algorithm is O(n), where n is the number of elements in the input list `nums`. 
# This is because the algorithm processes the list in a few linear passes: first to filter out non-positive numbers, then to mark the presence of positive numbers, 
# and finally to identify the first missing positive integer. Each of these operations involves iterating through the list, resulting in a total linear time complexity.

# Space Complexity:
# The space complexity is O(1) in terms of additional space used, 
# as the algorithm modifies the input list in place and does not utilize any significant extra space that scales with the input size. 
# The only space used is for a few variables, which is constant regardless of the input size. Thus, the algorithm is efficient in both time and space.

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