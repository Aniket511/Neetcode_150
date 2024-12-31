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

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        # Step 1: Filter out all non-positive numbers from the list (e.g., numbers <= 0)
        # Since the first missing positive number is always greater than 0, 
        # we can ignore non-positive numbers (negative numbers and zeros).
        nums = [number for number in nums if number > 0]

        # Step 2: Use the list `nums` to mark which positive integers exist in the list.
        # For each number `number` in the list, mark the corresponding index `number-1` as visited (by making it negative).
        for number in nums:
            # Get the index corresponding to the value `number` (i.e., for number 1, it's index 0, for number 2, it's index 1, etc.)
            # We use absolute value to handle already visited (negative) indices.
            idx = abs(number) - 1
            
            # Only mark the index if it's within the valid range (0 to len(nums)-1) and if the value at that index is positive.
            # If the value at `nums[index]` is positive, this means we haven't visited it yet.
            if idx < len(nums) and nums[idx] > 0:
                # Mark the number at the calculated index as visited by making it negative
                nums[idx] *= - 1

        # Step 3: Check the first index in the list where the number is still positive
        # If any index `i` has a positive value, it means `i + 1` is the missing positive number.
        for idx in range(len(nums)):
            if nums[idx] > 0:
                return idx + 1

        # Step 4: If no positive number is found, the first missing positive is `len(nums) + 1`
        return len(nums) + 1

# Time Complexity: O(n)
#     Filtering non-positive numbers: O(n), where n is the number of elements in the input list nums.
#     Marking the numbers: O(n), as we iterate through the list once.
#     Finding the first missing positive: O(n), as we again iterate through the list.
# Thus, the overall time complexity is O(n), where n is the size of the input list.

# Space Complexity: O(1)
# In-place modifications: No extra space is used other than modifying the nums array itself, so the space complexity is O(1) (ignoring the input array).

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