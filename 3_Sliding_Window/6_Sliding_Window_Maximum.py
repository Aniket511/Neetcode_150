"""
Sliding Window Maximum

Hard

You are given an array of integers nums, 
there is a sliding window of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        max_values = []
        queue = deque()
        for idx, val in enumerate(nums):
            while queue and val > queue[-1]:
                queue.pop()
            queue.append(val)
            if idx >= k and queue[0] == nums[idx - k]:
                queue.popleft()
            if idx >= k - 1:
                max_values.append(queue[0])
        return max_values

test_cases = [
    ([3,5,2,1,4,5,6,4,3,2,4,3,2,3,4,5,6,7,5,4], 3, [5, 5, 4, 5, 6, 6, 6, 4, 4, 4, 4, 3, 4, 5, 6, 7, 7, 7])
]

solution = Solution()

for idx, (nums, k, expected) in enumerate(test_cases):
    result = solution.maxSlidingWindow(nums, k)
    if result == expected:
        print(f"Test Case {idx + 1} Passed")
    else:
        print(f"Test Case {idx + 1} Failed, Expected: {expected}, Got: {result}")