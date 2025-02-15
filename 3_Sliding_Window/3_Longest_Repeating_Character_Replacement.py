"""
Longest Repeating Character Replacement

Medium

You are given a string s and an integer k. 
You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
"""

# Solution:

class Solution:
    def characterReplacement(self, array, k):
        # Dictionary to count the frequency of each character in the current window.
        frequency = {}
        # Initialize the left pointer, the result (max window length found), 
        # and max_frequency (frequency of the most frequent character in the window).
        left = result = max_frequency = 0
        
        # Iterate over the array with the right pointer.
        for right, letter in enumerate(array):
            # Update the count for the current character.
            frequency[letter] = frequency.get(letter, 0) + 1
            
            # Update max_frequency with the count of the current character,
            # this represents the most common character's frequency in the current window.
            max_frequency = max(max_frequency, frequency[letter])
            
            # Check if the current window is invalid:
            # (window size - frequency of most common character) gives the number of replacements needed.
            # If this number is greater than k, the window is too big and needs to shrink.
            while (right - left + 1) - max_frequency > k:
                # Decrease the frequency of the character at the left pointer
                frequency[array[left]] -= 1
                # Move the left pointer to shrink the window.
                left += 1
            
            # Update the result with the maximum valid window size found.
            result = max(result, right - left + 1)
        
        return result

# Time Complexity
#     O(n), where n is the length of the input array.
#     The algorithm uses a sliding window that expands and contracts over the array exactly once, making the iteration linear in the size of the array.

# Space Complexity
#     O(1) in most typical cases (e.g., when the input consists of a fixed set of characters such as English letters).
#     Even though a dictionary is used to count character frequencies, the maximum number of keys is limited by the size of the character set (which is constant).
#     In a worst-case scenario with an unbounded set of characters, the space complexity could be O(n).

test_cases = [
    ('ASACAD', 3, 6),
    ('ABCDEF', 2, 3),
    ('ABAB', 2, 4),
    ("AABABBA", 1, 4),
]

solution = Solution()
for idx, (s, k, expected) in enumerate(test_cases):
    result = solution.characterReplacement(s, k)
    if result == expected:
        print(f"Test Case {idx + 1} Passed")
    else:
        print(f"Test Case {idx + 1} Failed. Expected: {expected}, Got: {result}")