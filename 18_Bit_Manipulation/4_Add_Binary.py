"""
Amazon

Add Binary

Easy

Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []  # Initialize a list to store the binary result.
        carry = 0  # Initialize the carry to handle binary addition overflow.

        # Set pointers to the last character of both strings.
        i, j = len(a) - 1, len(b) - 1

        # Continue while either string has characters left, or there's a carry.
        while i >= 0 or j >= 0 or carry > 0:
            # Extract the binary digit from string `a` if within bounds; otherwise, use 0.
            digitA = int(a[i]) if i >= 0 else 0
            
            # Extract the binary digit from string `b` if within bounds; otherwise, use 0.
            digitB = int(b[j]) if j >= 0 else 0

            # Compute the sum of the current digits and the carry.
            total = digitA + digitB + carry
            
            # Append the remainder when total is divided by 2 (binary digit).
            res.append(total % 2)
            
            # Update the carry (integer division by 2).
            carry = total // 2

            # Move the pointers to the previous digits in both strings.
            i -= 1
            j -= 1

        # Since digits were appended in reverse order, reverse the result list.
        res.reverse()
        
        # Join the list of digits into a string and return.
        return ''.join(map(str, res))

# Time Complexity
#     Main Loop: The loop iterates over the larger of the two strings, plus one extra iteration if there’s a carry. 
#     If m=len(a) and n=len(b), the loop runs O(max⁡(m,n)).
#     Reverse Operation: Reversing the list res takes O(max⁡(m,n)).
#     Join Operation: Joining the list into a string takes O(max⁡(m,n)).
# Thus, the total time complexity is:
# O(max⁡(m,n))

# Space Complexity
#     Result List (res): The list res stores at most O(max⁡(m,n)+1) binary digits (due to potential carry).
#     Auxiliary Space: The algorithm uses O(1) space for pointers, carry, and intermediate variables.
# Thus, the total space complexity is:
# O(max⁡(m,n))
