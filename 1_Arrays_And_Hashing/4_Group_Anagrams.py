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

# Solution: Hashtable
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:   
        # Step 1: Initialize a defaultdict to store grouped anagrams.
        # defaultdict will automatically create a list for each unique key.
        result = defaultdict(list)

        # Step 2: Iterate through each word in the input list 'strs'.
        for word in strs:
            # Step 3: Initialize a count array of size 26 to store the frequency
            # of each letter in the current word. The array will have one element
            # for each letter from 'a' to 'z'.
            count = [0] * 26

            # Step 4: For each letter in the word, calculate its index in the count array.
            # Update the frequency count of the letter by incrementing the corresponding index.
            for letter in word:
                count[ord(letter) - ord('a')] += 1  # ord('a') ensures we start at index 0 for 'a'

            # Step 5: Convert the count list to a tuple (since lists are mutable and tuples are hashable).
            # The tuple will be used as the key in the 'result' dictionary.
            result[tuple(count)].append(word)  # Append the current word to the appropriate list

        # Step 6: Return the grouped anagrams. The values of the 'result' dictionary
        # are the lists of anagrams, so we return them as a list of lists.
        return list(result.values())

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
