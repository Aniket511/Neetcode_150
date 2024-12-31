"""
Facebook

Encode and Decode Strings

Medium

Design an algorithm to encode a list of strings to a single string. 
The encoded string is then decoded back to the original list of strings.
Please implement encode and decode

Example 1:
Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]

Example 2:
Input: ["we","say",":","yes"]
Output: ["we","say",":","yes"]
"""

# Solution :Encoding and Decoding
class Solution:
    
    def encode(self, strs: list[str]) -> str:
        # Initialize an empty result string
        encoded_string = ""
        
        # Loop over each string in the input list
        for string in strs:
            # For each string, append the length of the string, followed by a '#' character, 
            # then the string itself to the result string
            encoded_string += str(len(string)) + "#" + string
        
        # Return the final encoded string
        return encoded_string

    def decode(self, s: str) -> list[str]:
        # Initialize an empty list to store the decoded strings
        decoded_strings = []
        
        # Initialize a pointer to track the current position in the encoded string
        i = 0
        
        # Loop until we've processed the entire string
        while i < len(s):
            # Find the index of the '#' character, which separates the length of the string
            # from the string itself
            j = i
            while s[j] != '#':
                j += 1
            
            # Extract the length of the current string (before the '#' character)
            length = int(s[i:j])
            
            # Move the pointer i past the '#' character
            i = j + 1
            
            # The actual string starts at the position i and ends at i + length
            current_string = s[i:i + length]
            
            # Append the decoded string to the list of decoded strings
            decoded_strings.append(current_string)
            
            # Move the pointer i to the end of the current string
            i = i + length
        
        # Return the list of decoded strings
        return decoded_strings


# Time Complexity:
# O(n) where n is the sum of length of all strings for both encoding and decoding

# Space Complexity:
# O(1)  for encoding and decoding becasue we are not creating extra space

test_cases = [
    (["hello", "world"], "5#hello5#world", ["hello", "world"]),
    (["a", "bc", "defg"], "1#a2#bc4#defg", ["a", "bc", "defg"]),
    ([], "", []),  # Edge case: empty list
    (["", "", ""], "0#0#0#", ["", "", ""]),  # list with empty strings
    (["longstring", "anotherlongstring", "yetanother"], "10#longstring17#anotherlongstring10#yetanother", ["longstring", "anotherlongstring", "yetanother"]),
    (["abc", "", "defg", "xyz"], "3#abc0#4#defg3#xyz", ["abc", "", "defg", "xyz"]),
    (["!@#", "1234", "abcd$"], "3#!@#4#12345#abcd$", ['!@#', '1234', 'abcd$']),
]

solution = Solution()

# Test encode and decode
for i, (strs, expected_encoded, expected_decoded) in enumerate(test_cases):
    # Test encoding
    encoded = solution.encode(strs)
    decode_result = solution.decode(encoded)
    
    print(f"Test Case {i + 1} - Encoding:")
    print(f"  Expected Encoded: {expected_encoded}, Got: {encoded}")
    print(f"  Expected Decoded: {expected_decoded}, Got: {decode_result}")
    print(f"  {'Pass' if encoded == expected_encoded and decode_result == expected_decoded else 'Fail'}\n")