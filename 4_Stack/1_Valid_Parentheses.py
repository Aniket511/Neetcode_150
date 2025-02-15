"""
Valid Parentheses

Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true
"""

# Solution:
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        for bracket in s:
            if bracket in parentheses:
                if stack and stack[-1] == parentheses[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        return True

# Test Cases:
test_cases = [
    ("()", True),
    (")", False),
    ("(", True),
    ("(}", False),
    ("[}", False),
    ("(((((())))))", True),
    ("{(){)({)()})})}", False),
    ("({[{[()]}]})" ,True),
]

solution = Solution()
for idx, (s, expected) in enumerate(test_cases):
    result = solution.isValid(s)
    if result == expected:
        print(f"Test Case {idx + 1} Passed")
    else:
        print(f"Test Case {idx + 1} Failed. Expected: {expected}, Got: {result}")