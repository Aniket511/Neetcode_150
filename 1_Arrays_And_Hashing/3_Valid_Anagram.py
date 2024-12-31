"""
Uber 

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

# Solution 1: 2 Hashmaps (for both lowercase and uppercase)
class Solution1:
    def isAnagram1(self, s: str, t: str) -> bool:  
        # Step 1: Check Lengths
        # If the lengths of strings 's' and 't' are not equal, return False
        if len(s) != len(t):
            return False
        # Step 2: Count characters in 's'
        # Create a dictionary 'frequency' to store each count of each character in string 's'
        frequency = {}
        # Loop through each character in string 's'
        for character in s:
            # Use frequency.get(character, 0) to retrieve the current count of character in the dictionary. 
            # If character is not in the dictionary, default to 0.
            frequency[character] = frequency.get(character, 0) + 1
        # Step 3: Check characters in t
        # Loop through each character 'character' in string 't'
        for character in t:
            # Check if 'character' is not in the 'frequency' dictionary or if its count is already 0.
            # e.g. ['aab'] and ['abb'] 
            # If either condition is met, return False
            if character not in frequency or frequency[character] == 0:
                return False
            # If character is in frequency then decrement the count of character by 1
            frequency[character] -= 1
        # Step 4: Final Result
        # If the loop completes without returning False, it means all characters in s and t match count,
        # and the function returns true
        return True

# Time Complexity:
# O(n) where n is the length of the strings `s` and `t`. This is because the function iterates through each string once: 
# first to count the characters in `s` and then to check the characters in `t`. Since both strings must be of equal length for the function to proceed,
# the overall complexity remains linear with respect to the length of the strings 

# Space Complexity:
# The space complexity of the function is O(1) in terms of the character set size. 
# This is because the frequency dictionary will store counts for a limited number of characters (e.g., 26 lowercase letters, 26 uppercase letters, or 10 digits), 
# which is a constant size regardless of the input string length. 
# Therefore, while the space used by the frequency dictionary can be considered O(1) in terms of the character set, 
# it can also be viewed as O(k) where k is the size of the character set being used (e.g., 52 for uppercase and lowercase English letters)

# Test Cases:
test_cases1 = [
    (['anagram', 'nagaram'], True),
    (['rat', 'cat'], False),
    (['a', 'b'], False),
    (['racecar', 'caracer'], True),
]

solution1 = Solution1()
for i, (strs, expected) in enumerate(test_cases1):
    # Unpack the list into two separate strings
    s, t = strs
    result = solution1.isAnagram1(s, t)
    print(f"Test Case {i + 1}: {'Pass' if result == expected else 'Fail'} (Expected {expected}, Got {result})")