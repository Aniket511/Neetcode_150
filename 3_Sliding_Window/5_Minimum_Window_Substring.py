"""
Minimum Window Substring

Hard

Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s):
            return ""
        count_S, count_T = {}, {}
        for letter in t:
            count_T[letter] = count_T.get(letter, 0) + 1
        have, need = 0, len(count_T)
        result, result_length = [-1, -1], float("infinity")
        left = 0
        for right, letter in enumerate(s):
            count_S[letter] = count_S.get(letter, 0) + 1
            if letter in count_T and count_S[letter] == count_T[letter]:
                have += 1
                while have == need:
                    if (right - left + 1) < result_length:
                        result = [left, right]
                        result_length = (right - left + 1)
                    count_S[s[left]] -= 1
                    if s[left] in count_T and count_S[s[left]] < count_T[s[left]]:
                        have -= 1
                    left += 1
        left, right = result
        return s[left : right + 1] if result_length != float("infinity") else ""
            
test_cases = [
    ("CCCCCCBBBBBBCA", "ABC", "BCA"),
    ("ABXCDFERHGINFJLAMZNIFODHWQWROPWIEGOXHNCZKLB", "AX", "ABX"),
    ("", "", ""),
    ("VFS", "", ""),
    ("", "ASD", ""),
    ("ABCDFERHGINFJLAMZNIFODHWQWRAOPWIEGOXHNCZKL", "AX", "AOPWIEGOX"),
    ("ABCDFERHGXINFJLAMZNIFODHWQWROPWIEGOXHNCZKL", "AX", "XINFJLA"),
    ("ADOBECODEBANC", "ABC", "BANC"),
    ("a", "b", ""),
]
solution = Solution()

for idx, (s, t, expected) in enumerate(test_cases):
    output = solution.minWindow(s, t)
    if output == expected:
        print(f"Test Case {idx + 1} Passed")
    else:
        print(f"Test Case {idx + 1} Failed, Expected: {expected}, Got: {output}")