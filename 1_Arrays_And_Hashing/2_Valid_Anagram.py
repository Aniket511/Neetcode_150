"""
Valid Anagram

Easy
Given two strings s and t, return true if t is an anagram of s, and false otherwise. 

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""

# Solution 1: 2 Hashmaps
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:    
        # Step 1: Check if the lengths of both strings are the same
        if len(s) != len(t):
            # If not, return False
            return False
        
        # Step 2: Initialize two hashmaps (dictionaries) for both strings
        s_count = {}
        t_count = {}
        
        # Iterate through the indices for the length of either string
        for idx in range(len(s)):
            # Count characters for string `s`
            s_count[s[idx]] = 1 + s_count.get(s[idx], 0)
            # Count characters for string `t`
            t_count[t[idx]] = 1 + t_count.get(t[idx], 0)
        
        # Step 3: Return whether both hashmaps are the same
        return s_count == t_count

test_cases = [
    ("anagram", "nagaram", True),   # Both are anagrams
    ("rat", "car", False),         # Different lengths, not anagrams
    ("aabbcc", "bbaacc", True),    # Both are anagrams
    ("hello", "world", False),     # Not anagrams
    ("", "", True),                # Both are empty strings
    ("a", "ab", False),            # Different lengths
]

solution1 = Solution1()
for i, (s, t, expected) in enumerate(test_cases):
    result = solution1.isAnagram(s, t)
    print(f"Test Case {i+1}: {'Passed' if result == expected else 'Failed'}")

# Solution 2: Frequency Array
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:  
        # Step 1: Check if the lengths of both strings are the same
        if len(s) != len(t):
            return False

        # Step 2: Initialize a frequency array of size 26 for English lowercase letters
        count = [0] * 26

        # Step 3: Count character frequencies for string `s`
        for character in s:
            count[ord(character) - ord('a')] += 1

        # Step 4: Decrease character frequencies based on string `t`
        for character in t:
            if count[ord(character) - ord('a')] == 0:
                # If a character in `t` has no corresponding count in `s`, return False
                return False
            count[ord(character) - ord('a')] -= 1

        # Step 5: If all character counts balance out, the strings are anagrams
        return True

test_cases = [
    ("anagram", "nagaram", True),   # Both are anagrams
    ("rat", "car", False),         # Different lengths, not anagrams
    ("aabbcc", "bbaacc", True),    # Both are anagrams
    ("hello", "world", False),     # Not anagrams
    ("", "", True),                # Both are empty strings
    ("a", "ab", False),            # Different lengths
    ("abc", "cba", True),          # Anagrams with reversed order
]

solution2 = Solution2()
for i, (s, t, expected) in enumerate(test_cases):
    result = solution2.isAnagram(s, t)
    print(f"Test Case {i+1}: {'Passed' if result == expected else 'Failed'}")