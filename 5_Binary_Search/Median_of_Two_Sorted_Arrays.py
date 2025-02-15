"""
Median of Two Sorted Arrays

Hard

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
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

class Solution:
    def findMedianSortedArrays(self, array1: list[int], array2: list[int]) -> float:
        smaller_array = array1
        larger_array = array2
        total_length = len(larger_array) + len(smaller_array)
        half_length = total_length // 2
        if len(smaller_array) > len(larger_array):
            smaller_array, larger_array = larger_array, smaller_array
        left = 0
        right = len(smaller_array) - 1
        while True:
            partition_smaller = (left + right) // 2
            partition_larger = half_length - partition_smaller - 2

            if partition_smaller >= 0:
                smaller_left = smaller_array[partition_smaller]
            else:
                smaller_left = float('-infinity')

            if (partition_smaller + 1) < len(smaller_array):
                smaller_right = smaller_array[partition_smaller + 1]
            else:
                smaller_right = float('infinity')

            if partition_larger >= 0:
                larger_left = larger_array[partition_larger]
            else:
                larger_left = float('-infinity')

            if (partition_larger + 1) < len(larger_array):
                larger_right = larger_array[partition_larger + 1]
            else:
                larger_right = float('infinity')

            if smaller_left <= larger_right and larger_left <= smaller_right:
                if total_length % 2:
                    return min(smaller_right, larger_right) 
                else:
                    return (max(smaller_left, larger_left) + min(smaller_right, larger_right)) / 2
            elif smaller_left > larger_right:
                right = partition_smaller - 1
            else:
                left = partition_smaller + 1

solution = Solution()

test_cases = [
    ([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5], 3),
    ([1, 2], [3, 4], 2.5),
    ([1, 3], [2], 2),
    ([21, 22, 23, 24, 25, 26, 77, 88, 99, 100],[12, 13, 14, 15, 16, 17, 18, 19], 21.5)
]
for idx , (array1, array2, expected) in enumerate(test_cases):
    result = solution.findMedianSortedArrays(array1, array2)
    if result == expected:
        print(f"Test Case {idx + 1} Passed, expected: {expected}, got: {result}")
    else:
        print(f"Test Case {idx + 1} Failed, expected: {expected}, got: {result}")