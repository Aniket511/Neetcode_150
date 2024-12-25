"""
Spotify

Valid Palindrome

Easy

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

# Solution: Two Pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers, left starting from the beginning of the string and 
        # right starting from the end of the string.
        left, right = 0, len(s) - 1
        # Iterate as long as left pointer is less than the right pointer.
        while left < right:
            # Skip over non-alphanumeric characters from the left side.
            while left < right and not self.isalphaNum(s[left]):
                left += 1  # Move the left pointer to the right.
            # Skip over non-alphanumeric characters from the right side.
            while right > left and not self.isalphaNum(s[right]):
                right -= 1  # Move the right pointer to the left.
            # Check if the characters at the left and right pointers are the same (ignoring case).
            # If they are not the same, return False because it's not a palindrome.
            if s[left].lower() != s[right].lower():
                return False
            # Move the pointers towards the center of the string.
            left, right = left + 1, right - 1
        # If we have checked all pairs of characters and they matched, return True.
        return True
    def isalphaNum(self, character):
        # Helper function to check if a character is alphanumeric (i.e., a letter or a number).
        # This function returns True if the character is alphanumeric, otherwise False.
        return (ord('A') <= ord(character) <= ord('Z') or  # Check if the character is an uppercase letter.
                ord('a') <= ord(character) <= ord('z') or  # Check if the character is a lowercase letter.
                ord('0') <= ord(character) <= ord('9'))   # Check if the character is a digit (0-9).

# Time Complexity:
# The algorithm runs in O(n) time where n is the length of the string s. 
# This is because we only need to pass through the string once, 
# with each pointer (left and right) moving inward one step at a time.

# Space Complexity:
# The space complexity is O(1), since we only use a fixed amount of extra space 
# (just the two pointers and the helper function). 
# The string itself is not modified in place

# Test Cases:
test_cases = [
    ("A man, a plan, a canal, Panama", True),  # Classic palindrome with spaces and punctuation
    ("race a car", False),  # Not a palindrome, because of extra characters and mismatch
    ("", True),  # Empty string is considered a palindrome
    ("a", True),  # A single character string is a palindrome
    ("ab", False),  # A two-character string where characters don't match
    ("No 'x' in Nixon", True),  # Palindrome with mixed case and punctuation
    ("12321", True),  # Palindrome with digits
    ("12345", False),  # Not a palindrome with digits
    ("Was it a car or a cat I saw?", True),  # Palindrome with punctuation, case insensitivity
    ("", True),  # Empty string is trivially a palindrome
    ("Madam In Eden, I'm Adam", True),  # Palindrome with mixed case and punctuation
    ("Hello, World!", False),  # Not a palindrome, mixed case and punctuation
]

solution = Solution()
for i, (s, expected) in enumerate(test_cases):
    result = solution.isPalindrome(s)
    print(f"Test Case {i + 1}: {'Pass' if result == expected else 'Fail'} (Expected {expected}, Got {result})")