"""
Longest Substring Without Repeating Characters

Medium

Given a string s, find the length of the longest
substring
without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

# Solution:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # This dictionary will record the latest index where each character was seen.
        letter_index = {}
        # Variable to keep track of the length of the longest substring without repeating characters.
        max_length = 0
        # 'left' represents the starting index of the current substring window.
        left = 0
        
        # Loop through each character in the string, where 'right' is the current index and 'letter' is the character.
        for right, letter in enumerate(s):
            # If the letter has been encountered before and its last seen index is within the current window, i.e.. left idx position is before repeated character idx
            # move the 'left' pointer to just after that index to avoid having duplicate letters in the window.
            if letter in letter_index and letter_index[letter] >= left:
                left = letter_index[letter] + 1
            
            # Update the dictionary with the current index for the letter.
            letter_index[letter] = right
            
            # Calculate the size of the current window and update max_length if it's larger than the previous value.
            max_length = max(max_length, right - left + 1)
        
        # Return the length of the longest substring found that does not contain any repeating characters.
        return max_length


# Time Complexity: 
#   O(n), where n is the length of the string, since each character is visited once.

# Space Complexity: 
#   O(n) in the worst-case scenario, where all characters in the string are unique.


test_cases = [
    ("ajnfjknskejv", 6),
    ("aaaaaaaa", 1),
    ("abcdefghijklmnopqrstuvwxyz", 26),
    ("", 0)
]

solution = Solution()
for idx, (s, expected) in enumerate(test_cases):
    result = solution.lengthOfLongestSubstring(s)
    if result == expected:
        print(f"Test Case {idx + 1} Passed")
    else:
        print(f"Test Case {idx + 1} Failed. Expected: {expected}, Got: {result}")