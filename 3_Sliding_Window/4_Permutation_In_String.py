"""
Permutation in String

Medium

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's1, s2 permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""

# Solution:

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Get the lengths of s1 and s2
        n1 = len(s1)
        n2 = len(s2)
        
        # If s1 is longer than s2, it's impossible for s1's permutation to be in s2.
        if n1 > n2:
            return False
        
        # Initialize frequency counters for s1 and the current window in s2.
        # We use a fixed-size list of 26 elements (for each lowercase letter).
        count_s1 = [0] * 26
        count_s2 = [0] * 26

        # Count the frequency of each letter in s1 and the first window (of size n1) in s2.
        for idx in range(n1):
            count_s1[ord(s1[idx]) - ord('a')] += 1
            count_s2[ord(s2[idx]) - ord('a')] += 1

        # Check if the first window in s2 is a permutation of s1.
        if count_s1 == count_s2:
            return True

        # Slide the window across s2, one character at a time.
        for idx in range(n1, n2):
            # Include the new character in the current window.
            count_s2[ord(s2[idx]) - ord('a')] += 1
            # Exclude the character that is no longer in the window.
            count_s2[ord(s2[idx - n1]) - ord('a')] -= 1
            # Check if the current window's frequency matches that of s1.
            if count_s1 == count_s2:
                return True

        # If no matching window is found, return False.
        return False

# Time Complexity
#     O(n1): Building the initial frequency count for the first window (where n1 is the length of s1).
#     O(n2 - n1): Sliding the window through the rest of s2, updating the count arrays, and comparing them. 
#     Each window update and comparison takes constant time because the count arrays have a fixed size of 26.
#     Overall: The algorithm runs in O(n2) time, where n2 is the length of s2.

# Space Complexity
#     O(1): The extra space used is the two frequency arrays count_s1 and count_s2, each of fixed size 26 (independent of the input size). Thus, the space complexity is constant.

test_cases = [
    ("ab", "eidbaooo", True),
    ("ab", "eidboaoo", False)
]

solution = Solution()
for idx, (s1, s2, expected) in enumerate(test_cases):
    result = solution.checkInclusion(s1, s2)
    if result == expected:
        print(f"Test Case {idx + 1} Passed")
    else:
        print(f"Test Case {idx + 1} Failed. Expected: {expected}, Got: {result}")