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
        # Initialize a list `dp` with n+1 elements, all set to 0.
        # `dp[i]` will store the number of 1's in the binary representation of `i`.
        dp = [0] * (n + 1)
        
        # Loop through all numbers from 0 to n.
        for i in range(n + 1):
            # The number of 1's in `i` is the same as the number of 1's in `i >> 1`
            # (i divided by 2, which shifts the binary representation one bit to the right)
            # plus 1 if the least significant bit of `i` is 1 (i.e., `i & 1`).
            dp[i] = dp[i >> 1] + (i & 1)
        
        # Return the list containing the number of 1's for each number from 0 to n.
        return dp

# Time Complexity: O(n)
# The algorithm iterates from 0 to n, performing constant-time operations for each value of i.
#     Loop iteration: The loop runs O(n+1) times (from 0 to n inclusive).
#     Work per iteration: Calculations such as i >> 1 and i & 1 are O(1) operations.
# Thus, the overall time complexity is: O(n)

# Space Complexity: O(n)
#     Space for the dp list: The list dp stores n+1n+1 elements, requiring O(n) space.
#     Auxiliary space: The algorithm uses only a constant amount of additional space for variables like i.
# Thus, the overall space complexity is: O(n)

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
