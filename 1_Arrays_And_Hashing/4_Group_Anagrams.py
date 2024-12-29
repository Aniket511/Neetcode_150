"""
Amazon 

Group Anagrams

Medium

Given an array of strings strs, group the anagrams together. You can return the answer in any order. 

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:

    There is no string in strs that can be rearranged to form "bat".
    The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
    The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""

# Solution 1: Hashtable
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Dictionary to hold the group of words (anagrams) based on their letter frequency count
        group = {}
        
        # Iterate through each word in the list
        for word in strs:
            # Create a list to count the frequency of each letter (from 'a' to 'z')
            count = [0] * 26
            
            # Count frequency of each character in the word
            for letter in word:
                count[ord(letter) - ord('a')] += 1
            
            # Convert the frequency count list to a tuple, so it can be used as a dictionary key
            count_tuple = tuple(count)
            
            # Add the word to the corresponding anagram group
            if count_tuple not in group.keys():
                group[count_tuple] = [word]
            else:
                group[count_tuple].append(word)
        
        # Return the values of the dictionary (groups of anagrams)
        return list(group.values())


# Time Complexity:
# O(m + n) where m is the length of longest string and n is the number of string

# Space Complexity:
# O(n) where n is the number of strings

# Test Cases:
test_cases = [
    (["eat", "tea", "tan", "ate", "nat", "bat"], [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]),
    ([""], [[""]]),
    (["a"], [['a']]),
    (["abc", "bca", "cab", "cba", "bac"], [['abc', 'bca', 'cab', 'cba', 'bac']]),
    (["abc", "def", "ghi", "jkl"], [['abc'], ['def'], ['ghi'], ['jkl']]),
    (["abcd", "bcda", "cdab", "dcba", "xyz", "yzx"], [['abcd', 'bcda', 'cdab', 'dcba'], ['xyz', 'yzx']]),
    (["", "", "bat", "tab", "pat"], [['', ''], ['bat', 'tab'], ['pat']]),
    (["rose", "ores", "hello", "ohlle", "bat", "tab"], [['rose', 'ores'], ['hello', 'ohlle'], ['bat', 'tab']]),
    (["longword", "wordlong", "gnolword", "wordnolg"], [['longword', 'wordlong', 'gnolword', 'wordnolg']]),
    (["a", "b", "c", "ab", "ba"], [['a'], ['b'], ['c'], ['ab', 'ba']])
]

solution = Solution()  
for i, (strs, expected) in enumerate(test_cases):
    result = solution.groupAnagrams(strs)
    print(f"Test Case {i + 1}: {'Pass' if result == expected else 'Fail'} (Expected {expected}, Got {result})")