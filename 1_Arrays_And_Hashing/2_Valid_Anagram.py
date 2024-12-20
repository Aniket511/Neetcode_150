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
        # Create a dictionary 'counter' to store each count of each character in string 's'
        counter = {}
        # Loop through each character in string 's'
        for char in s:
            # Use counter.get(char, 0) to retrieve the current count of char in the dictionary. 
            # If char is not in the dictionary, default to 0.
            counter[char] = counter.get(char, 0) + 1
        # Step 3: Check characters in t
        # Loop through each character 'char' in string 't'
        for char in t:
            # Check if 'char' is not in the 'counter' dictionary or if its count is already 0.
            # e.g. ['aab'] and ['abb'] 
            # If either condition is met, return False
            if char not in counter or counter[char] == 0:
                return False
            # If char is in counter then decrement the count of char by 1
            counter[char] -= 1
        # Step 4: Final Result
        # If the loop completes without returning False, it means all characters in s and t match count,
        # and the function returns true
        return True

# Time Complexity:
# O(n) because we iterate through all the characters of  s at least once

# Space Complexity:
# O(52) -> O(1) because both strings consist of alphabets


# Test Cases:
test_cases = [
    (['anagram', 'nagaram'], True),
    (['rat', 'cat'], False),
    (['a', 'b'], False),
    (['racecar', 'caracer'], True)
]

solution1 = Solution1()
for i, (strs, expected) in enumerate(test_cases):
    # Unpack the list into two separate strings
    s, t = strs
    result = solution1.isAnagram1(s, t)
    print(f"Test Case {i + 1}: {'Pass' if result == expected else 'Fail'} (Expected {expected}, Got {result})")


# Solution 2: Frequency Array (for all lowercase or all uppercase letters)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:  
        # Step 1: Check Lengths
        # If the lengths of strings 's' and 't' are not equal, return False
        if len(s) != len(t):
            return False
        # Step 2: Initialize Count Array
        # Create an array of size 26 (assuming input strings are lowercase letters)
        # Initialize all values of count as 0
        count = [0] * 26
        # Step 3: Count occurances in s
        # Iterate through each character char in string s. 
        # Increment the count of the corresponding letter in the count array.
        for char in s:
            # ord(char) returns the ASCII calue of the character
            # ord(char) - ord('a') maps 'a' to 0, 'b' to 2, ans so on
            count[ord(char) - ord('a')] += 1
        # Step 4:  Check occurances in t
        # Iterate through each character char in string t. 
        # If the count of the corresponding letter in the count array is already 0, 
        # return False because it means t has more occurrences of that letter than s
        for char in t:
            if count[ord(char) - ord('a')] == 0:
                return False
            # Decrement the count of the corresponding letter in count 
            # because it has been matched with a letter in t
            count[ord(char) - ord('a')] -= 1
        # Step 5: Check remaining result
        # Aftee both loops, check if all counts array are zero. 
        # If so, retrun True because every letter in s has been mathced with every letter in t
        return True

# Time Complexity:
# O(n) because we iterate through all the characters of  s at least once

# Space Complexity:
# O(26) -> O(1) because both strings consist of lowercase alphabets

# Test Cases:
test_cases = [
    (['anagram', 'nagaram'], True),
    (['rat', 'cat'], False),
    (['a', 'b'], False),
    (['racecar', 'caracer'], True)
]

solution = Solution()
for i, (strs, expected) in enumerate(test_cases):
    # Unpack the list into two separate strings
    s, t = strs
    result = solution.isAnagram(s, t)
    print(f"Test Case {i + 1}: {'Pass' if result == expected else 'Fail'} (Expected {expected}, Got {result})")