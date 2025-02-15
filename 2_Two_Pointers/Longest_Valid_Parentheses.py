"""
Longest Valid Parentheses

Hard

Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0
"""

class Solution:
    def longestValidParentheses(self, s):
        open_count = close_count = maximum_length = 0
        for idx in range(len(s)):
            if s[idx] == '(':
                open_count += 1
            else:
                close_count += 1
            if open_count == close_count:
                maximum_length = max(maximum_length, open_count + close_count)
            elif close_count > open_count:
                open_count = close_count = 0
        open_count = close_count = 0
        for idx in range(len(s) - 1, -1, -1):
            if s[idx] == ")":
                close_count += 1
            else:
                open_count += 1
            if close_count == open_count:
                maximum_length = max(maximum_length, close_count + open_count)
            elif open_count > close_count:
                open_count = close_count = 0
        return maximum_length

test_cases = [
    ("())((()()()(())))())()", 16),
    ("(()", 2),
    (")()())", 4),
    ("", 0),
    ("((((((()))))))", 14),
    ("())", 2),
    ("(()", 2)
]
solution = Solution()
for idx, (parentheses, expected) in enumerate(test_cases):
    result = solution.longestValidParentheses(parentheses)
    if result == expected:
        print(f"Test Case {idx + 1} Passed")
    else:
        print(f"Test Cases {idx + 1} Failed, Expected: {expected}, Got: {result}")