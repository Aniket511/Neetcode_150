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

class Solution:
    def encode(self, strs: list[str]) -> str:
        # If the input list is empty, return an empty string
        if not strs:
            return ""
        
        # `lengths` will store the length of each string in `strs`
        lengths, encoded_str = [], ""
        
        # Step 1: Record the lengths of each string in `strs`
        for string in strs:
            lengths.append(len(string))
        
        # Step 2: Encode the lengths of strings
        for length in lengths:
            encoded_str += str(length)  # Add the length as a string
            encoded_str += ','  # Use a comma as separator
        
        # Add a separator between lengths and actual strings
        encoded_str += '#'
        
        # Step 3: Append the actual strings to `encoded_str`
        for string in strs:
            encoded_str += string  # Add the string to the result
        
        # Return the fully encoded string
        return encoded_str

    def decode(self, encoded_str: str) -> list[str]:
        # If the encoded string is empty, return an empty list
        if not encoded_str:
            return []
        
        # `lengths` will store the lengths of the strings to be decoded
        lengths, decoded_strs, i = [], [], 0
        
        # Step 1: Extract lengths from the encoded string
        while encoded_str[i] != '#':
            length_str = ""
            # Extract the number (length of a string) from the encoded string
            while encoded_str[i] != ',':
                length_str += encoded_str[i]
                i += 1
            # Add the integer length to the `lengths` list
            lengths.append(int(length_str))
            i += 1  # Skip the comma
        
        # Step 2: Decode the actual strings based on the lengths
        i += 1  # Skip the '#' separator
        
        for length in lengths:
            decoded_strs.append(encoded_str[i:i + length])  # Extract the string of the given length
            i += length  # Move the index forward by the length of the string
        
        # Return the list of decoded strings
        return decoded_strs