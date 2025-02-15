class Solution:
    def integer_to_binary(self, val):
        # Make sure the value is between 0 and 1
        if val < 0 or val >= 1:
            print("Input must be a decimal number between 0 and 1.")
            return
        
        result = ''
        p = 0
        
        # We use a loop to generate the binary representation
        while p < 30:  # Limit the number of binary digits to prevent infinite loops
            val *= 2
            bit = int(val)
            result += str(bit)
            val -= bit
            p += 1
            if val == 0:
                break
        
        # The binary string generated will now be in the form "0.XXXX"
        print(f"The binary representation of {val} is 0.{result}")
    def binary_to_int(self, binary_str):
        # Check if the binary string is valid (only contains '0' and '1')
        if not all(char in '01' for char in binary_str):
            print("Invalid binary string. Please provide a string containing only '0' and '1'.")
            return
        
        # Convert binary string to integer
        integer_value = 0
        for i, bit in enumerate(binary_str):
            integer_value += int(bit) * (2 ** (len(binary_str) - 1 - i))
        
        return integer_value

# Example usage:
sol = Solution()
binary_str = "1011"  # Should return 11
result = sol.binary_to_int(binary_str)
print(f"The integer value of the binary string '{binary_str}' is {result}")

# Example usage:
sol.integer_to_binary(0.625)  # This should return 0.101
