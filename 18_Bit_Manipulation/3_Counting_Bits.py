"""
Amazon

Counting Bits

Easy

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
ans[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
"""

# Solution 1: Bit Manipulation (Optimal)
class Solution:
    def countBits(self, n: int) -> list[int]:
        dp = [0] * (n + 1)
        for i in range(n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp

# Test Cases:
test_cases = [
    (4, [0, 1, 1, 2, 1]),
    (2, [0, 1, 1]),
    (5, [0, 1, 1, 2, 1, 2]),
    (2, [0, 1, 1])
]

solution = Solution()
for i, (nums, expected) in enumerate(test_cases):
    result = solution.countBits(nums)
    print(f"Test Case {i + 1}: {'Pass' if result == expected else 'Fail'} (Expected {expected}, Got {result})")
