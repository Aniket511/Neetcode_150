"""
Longest Common Prefix

Easy

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

# Solution 1: using Enumerate
class Solution:
    def longestCommonPrefix(self, strs):
        # If the input list is empty, there is no common prefix
        if not strs:
            return ""
        
        # Iterate over each character and its index in the first string
        for idx, letter in enumerate(strs[0]):
            # Check the same position (idx) in all other words in the list
            for word in strs:
                # If we reach the end of a word or the character does not match:
                if idx == len(word) or word[idx] != letter:
                    # Return the common prefix found so far
                    return word[:idx]
        
        # If we complete the loop without finding a mismatch, the first string itself is the prefix
        return strs[0]

# Solution 2: Using range 
class Solution:
    def longestCommonPrefix(self, strs):
        # If the input list is empty, there is no common prefix
        if not strs:
            return ""
        
        # Iterate over the indices of the first string
        for idx in range(len(strs[0])):
            # Get the character at the current index from the first string
            character = strs[0][idx]
            # Compare this character with the character at the same index in all other words
            for word in strs:
                # If we reach the end of a word or characters do not match:
                if idx == len(word) or word[idx] != character:
                    # Return the common prefix found so far
                    return word[:idx]
        
        # If we complete the loop without finding a mismatch, the first string itself is the prefix
        return strs[0]

# Time Complexity:
# O(l * n), where n is the length of strs and l is the length of shortest word, because for each letter in shortest word of strs,
# we compare it with the corrseponding letter of all the other words in strs

# Space Complexity:
# O(1) The space complexity is O(1) since the algorithm uses a constant amount of extra space regardless of the input size. 
# It does not create any additional data structures that scale with the input; 
# it only uses a few variables for indexing and storing the current character being checked 

# Test Cases
test_cases = [
    (["flower", "flower", "flower"], 'flower'),
    (["flower", "flow", "flight"], 'fl'),
    (["dog", "racecar", "car"], ""),
]
solution = Solution()  
for i, (strs, expected) in enumerate(test_cases):
    result = solution.longestCommonPrefix(strs)
    print(f"Test Case {i + 1}: {'Pass' if result == expected else 'Fail'} (Expected {expected}, Got {result})")