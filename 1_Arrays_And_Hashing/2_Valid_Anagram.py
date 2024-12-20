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
        for character in s:
            # Use counter.get(character, 0) to retrieve the current count of character in the dictionary. 
            # If character is not in the dictionary, default to 0.
            counter[character] = counter.get(character, 0) + 1
        # Step 3: Check characters in t
        # Loop through each character 'character' in string 't'
        for character in t:
            # Check if 'character' is not in the 'counter' dictionary or if its count is already 0.
            # e.g. ['aab'] and ['abb'] 
            # If either condition is met, return False
            if character not in counter or counter[character] == 0:
                return False
            # If character is in counter then decrement the count of character by 1
            counter[character] -= 1
        # Step 4: Final Result
        # If the loop completes without returning False, it means all characters in s and t match count,
        # and the function returns true
        return True

# Time Complexity:
# O(n) because we iterate through all the characters of s at least once

# Space Complexity:
# O(52) -> O(1) because both strings consist of alphabets


# Test Cases:
test_cases1 = [
    (['anagram', 'nagaram'], True),
    (['rat', 'cat'], False),
    (['a', 'b'], False),
    (['racecar', 'caracer'], True)
]

solution1 = Solution1()
for i, (strs, expected) in enumerate(test_cases1):
    # Unpack the list into two separate strings
    s, t = strs
    result = solution1.isAnagram1(s, t)
    print(f"Test Case {i + 1}: {'Pass' if result == expected else 'Fail'} (Expected {expected}, Got {result})")


# Solution 2: Frequency Array (for all lowercase or all uppercase letters)
class Solution2:
    def isAnagram2(self, s: str, t: str) -> bool:  
        # Step 1: Check Lengths
        # If the lengths of strings 's' and 't' are not equal, return False
        if len(s) != len(t):
            return False
        # Step 2: Initialize Count Array
        # Create an array of size 26 (assuming input strings are lowercase letters)
        # Initialize all values of count as 0
        count = [0] * 26
        # Step 3: Count occurances in s
        # Iterate through each character character in string s. 
        # Increment the count of the corresponding letter in the count array.
        for character in s:
            # ord(character) returns the ASCII calue of the character
            # ord(character) - ord('a') maps 'a' to 0, 'b' to 2, ans so on
            count[ord(character) - ord('a')] += 1
        # Step 4:  Check occurances in t
        # Iterate through each character character in string t. 
        # If the count of the corresponding letter in the count array is already 0, 
        # return False because it means t has more occurrences of that letter than s
        for character in t:
            if count[ord(character) - ord('a')] == 0:
                return False
            # Decrement the count of the corresponding letter in count 
            # because it has been matched with a letter in t
            count[ord(character) - ord('a')] -= 1
        # Step 5: Check remaining result
        # Aftee both loops, check if all counts array are zero. 
        # If so, retrun True because every letter in s has been mathced with every letter in t
        return True

# Time Complexity:
# O(n) because we iterate through all the characters of s at least once

# Space Complexity:
# O(26) -> O(1) because both strings consist of lowercase alphabets

# Test Cases:
test_cases2 = [
    (['anagram', 'nagaram'], True),
    (['rat', 'cat'], False),
    (['a', 'b'], False),
    (['racecar', 'caracer'], True)
]

solution2 = Solution2()
for i, (strs, expected) in enumerate(test_cases2):
    # Unpack the list into two separate strings
    s, t = strs
    result = solution2.isAnagram2(s, t)
    print(f"Test Case {i + 1}: {'Pass' if result == expected else 'Fail'} (Expected {expected}, Got {result})")