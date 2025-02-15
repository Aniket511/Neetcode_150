"""
Subarrays with K Different Integers

Hard

Given an integer array nums and an integer k, return the number of good subarrays of nums.
A good array is an array where the number of different integers in that array is exactly k.
    For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

Example 2:
Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
"""

class Solution:
    def subarraysWithKDistinct(self, nums, k):
        # `count` is an array to track the frequency of numbers in the current window.
        # Its size is one more than the length of `nums` to account for all possible values.
        count = [0] * (len(nums) + 1)
        
        # `result` will store the total number of good subarrays.
        result = 0
        
        # `left` and `right` are pointers for managing the sliding window.
        # `left` marks the start of the subarray.
        # `right` helps in counting valid subarrays.
        left = right = 0
        
        # Iterate through each number in the array.
        for number in nums:
            # Increment the count of the current number in the window.
            count[number] += 1
            
            # If it's the first occurrence of `number`, decrease `k`.
            # This indicates a new distinct integer in the window.
            if count[number] == 1:
                k -= 1
                
                # If `k` becomes negative, we need to shrink the window.
                if k < 0:
                    # Reset the frequency of the number at `right` to 0 (effectively removing it).
                    count[nums[right]] = 0
                    
                    # Move `right` to the next position and reset `left`.
                    right += 1
                    left = right
            
            # If there are no more than `k` distinct integers in the window:
            if k <= 0:
                # Shrink the window from the left (`right`) until all elements in the window
                # are unique and valid (no duplicate numbers in excess).
                while count[nums[right]] > 1:
                    count[nums[right]] -= 1
                    right += 1
                
                # The number of valid subarrays ending at the current position is:
                # `right - left + 1` (subarrays starting from `left` to `right`).
                result += right - left + 1
        
        # Return the total count of valid subarrays.
        return result

test_case = [
    # Basic test cases
    ([1, 2, 1, 2, 3], 2, 7),  # Explained in the example
    ([1, 2, 1, 3, 4], 3, 3),  # Explained in the example

    # Edge cases
    ([1, 2, 3, 4, 5], 1, 5),  # Each single element is its own subarray
    ([1, 1, 1, 1, 1], 1, 15), # All subarrays are valid with 1 distinct number
    ([1, 2, 3, 4, 5], 5, 1),  # Entire array is the only subarray with 5 distinct numbers
    ([1, 2, 3, 4, 5], 6, 0),  # Impossible to have 6 distinct numbers

    # Cases with duplicate elements
    ([1, 2, 1, 2, 1], 2, 10), # Multiple overlapping subarrays with 2 distinct numbers
    ([1, 2, 1, 3, 2], 2, 5),  # Mixed duplicate elements with 2 distinct numbers

    # Cases with only one distinct number repeated
    ([1, 1, 1, 1], 2, 0),  # Not enough distinct numbers
    ([1, 1, 1, 1], 1, 10), # All subarrays are valid

    # Larger arrays
    ([1, 2, 3, 4, 1, 2, 3, 4], 3, 6), # Subarrays with 3 distinct numbers
    ([1, 2, 3, 4, 5, 6, 7, 8], 4, 5), # Larger array with 4 distinct numbers

    # Cases with a mix of increasing and repeating patterns
    ([1, 2, 3, 1, 2, 1, 3, 4], 3, 15), # Subarrays with 3 distinct numbers
    ([1, 1, 2, 2, 3, 3, 4, 4], 3, 8), # Structured repeating elements with 3 distinct numbers
]

solution = Solution()
for idx, (nums, k, expected) in enumerate(test_case):
    result = solution.subarraysWithKDistinct(nums, k)
    if result == expected:
        print(f"Test Case {idx + 1} Passed")
    else:
        print(f"Test Case {idx + 1} Failed, Expected: {expected}, Got: {result}")