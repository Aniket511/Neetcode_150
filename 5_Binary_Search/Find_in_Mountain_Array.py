"""
Find in Mountain Array

Hard

(This problem is an interactive problem.)
You may recall that an array arr is a mountain array if and only if:
    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.
You cannot access the mountain array directly. You may only access the array using a MountainArray interface:
    MountainArray.get(k) returns the element of the array at index k (0-indexed).
    MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

Example 1:
Input: mountainArr = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.

Example 2:
Input: mountainArr = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.
"""

class MountainArray:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index: int) -> int:
        return self.arr[index]

    def length(self) -> int:
        return len(self.arr)

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        start = 0
        end = mountainArr.length() - 1
        while start <= end:
            middle = (start + end) // 2
            if mountainArr.get(middle) < mountainArr.get(middle + 1):
                start = middle + 1
            else:
                end = middle - 1
        peak = start
        left = 0
        right = peak
        while left <= right:
            middle = (left + right) // 2
            if mountainArr.get(middle) == target:
                return middle
            elif mountainArr.get(middle) < target:
                left = middle + 1
            else:
                right = middle - 1
        left = peak + 1
        right = mountainArr.length() - 1
        while left <= right:
            middle = (left + right) // 2
            if mountainArr.get(middle) == target:
                return middle
            elif mountainArr.get(middle) < target:
                left = middle + 1
            else:
                right = middle - 1

# Testing the solution with the given example
mountain = MountainArray([1, 3, 5, 7, 6, 4, 2])
target = 5
# Create an instance of Solution
solution = Solution()
# Call the method on the instance of Solution
#
print(solution.findInMountainArray(target, mountain))  # Expected Output: 2