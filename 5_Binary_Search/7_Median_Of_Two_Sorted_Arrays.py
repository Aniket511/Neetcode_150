"""
Median of Two Sorted Arrays

Hard

Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)). 

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""

import math
from math import nan
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        # Get the lengths of the two arrays
        len1, len2 = len(nums1), len(nums2)
        
        # Set the range for binary search on nums1
        left, right = 0, len1
        
        while left <= right:
            # Partition nums1 and nums2
            partition1 = (left + right) // 2
            partition2 = (len1 + len2 + 1) // 2 - partition1
            
            # Find the maximum elements on the left of the partition
            max_left1 = nums1[partition1-1] if partition1 > 0 else float('-inf')
            max_left2 = nums2[partition2-1] if partition2 > 0 else float('-inf')
            max_left = max(max_left1, max_left2)
            
            # Find the minimum elements on the right of the partition
            min_right1 = nums1[partition1] if partition1 < len1 else float('inf')
            min_right2 = nums2[partition2] if partition2 < len2 else float('inf')
            min_right = min(min_right1, min_right2)
            
            # Check if the partition is correct
            if max_left <= min_right:
                # If the total length is even, return the average of the two middle elements
                if (len1 + len2) % 2 == 0:
                    return (max_left + min_right) / 2
                # If the total length is odd, return the middle element
                else:
                    return max_left
            elif max_left1 > min_right2:
                right = partition1 - 1
            else:
                left = partition1 + 1

# Test cases for findMedianSortedArrays
test_cases = [
    ([1, 3], [2], 2),
    ([1, 2], [3, 4], 2.5),
    ([], [1, 2, 3, 4, 5], 3),
    ([], [], math.nan),  # Handle empty arrays case, should return NaN
    ([i for i in range(1000000)], [i for i in range(1000000, 2000000)], 999999.5),
    ([1, 1, 1], [1, 1], 1),
    ([1, 3, 8], [7, 9, 10, 11], 8),
    ([-5, -3, -1], [-4, -2, 0], -2.5),  # Correct expected output as -2.5
    ([1000000000, 2000000000], [3000000000, 4000000000], 2500000000.0),
    ([1], [2], 1.5),
    ([1, 1000, 10000], [5000, 100000], 5000)
]

solution = Solution()

# Run the test cases
for i, (nums1, nums2, expected) in enumerate(test_cases):
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(f"Test Case {i + 1}: {'Pass' if (math.isnan(result) and math.isnan(expected)) or result == expected else 'Fail'} (Expected {expected}, Got {result})")