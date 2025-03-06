"""
Minimum Window Substring

Hard

Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Get the length of t. If t is longer than s or empty, there's no valid window.
        target_length = len(t)
        if target_length > len(s) or target_length == 0:
            return ""
        
        # Build a frequency dictionary for characters in t.
        target_char_count = {}
        for char in t:
            target_char_count[char] = target_char_count.get(char, 0) + 1
        
        # Initialize the smallest window (start, end) with an impossible high value.
        smallest_window = (0, len(s) + 1)
        window_start = 0  # Left pointer for the sliding window.
        required_chars = target_length  # Total number of characters we need to match t.
        
        # Iterate over s with window_end as the right pointer.
        for window_end, current_char in enumerate(s):
            # If current_char is part of t, update its count.
            if current_char in target_char_count:
                # Only decrement required_chars if the count is still positive.
                if target_char_count[current_char] > 0:
                    required_chars -= 1
                # Decrement the count for current_char in our frequency map.
                target_char_count[current_char] -= 1
            
            # When all required characters are in the window:
            if required_chars == 0:
                # Try to shrink the window from the left.
                while True:
                    start_char = s[window_start]
                    # If start_char isn't part of t, move the left pointer.
                    if start_char not in target_char_count:
                        window_start += 1
                        continue
                    # If removing start_char would break the valid window, stop shrinking.
                    if target_char_count[start_char] == 0:
                        break
                    # Otherwise, increment the count back (since it's an extra occurrence)
                    target_char_count[start_char] += 1
                    window_start += 1
                
                # Update the smallest window if the current window is smaller.
                if window_end - window_start + 1 < smallest_window[1] - smallest_window[0]:
                    smallest_window = (window_start, window_end + 1)
                
                # Prepare to search for a new window by moving window_start:
                # Increase the count of the character at window_start, since we will remove it.
                target_char_count[s[window_start]] += 1
                # This character is now missing from our window, so we need one more.
                required_chars += 1
                # Move the left pointer to effectively remove this character.
                window_start += 1
        
        # If smallest_window was updated, return the corresponding substring; otherwise, return "".
        return "" if smallest_window[1] > len(s) else s[smallest_window[0]:smallest_window[1]]