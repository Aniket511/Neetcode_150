"""
Number of 1 Bits

Easy

Given a positive integer n, 
write a function that returns the number of set bits
in its binary representation (also known as the Hamming weight).

Example 1:
Input: n = 11
Output: 3
Explanation:
The input binary string 1011 has a total of three set bits.

Example 2:
Input: n = 128
Output: 1
Explanation:
The input binary string 10000000 has a total of one set bit.

Example 3:
Input: n = 2147483645
Output: 30
Explanation:
The input binary string 1111111111111111111111111111101 has a total of thirty set bits.
"""

# Solution 1: Bitmask I
class Solution1:
    def hammingWeight(self, n: int) -> int:
        # Step 1: Initialize the result variable to 0
        # This will store the number of 1 bits in the binary representation of `n`.
        result = 0

        # Step 2: Loop over each bit of the 32-bit integer `n`
        for i in range(32):
            # Step 3: Check if the i-th bit is set (1)
            # The expression (1 << i) shifts the number 1 to the left by i positions.
            # By ANDing (&) with `n`, we isolate the i-th bit of `n`.
            if (1 << i) & n:
                # Step 4: If the bit is set (1), increment the result counter.
                result += 1

        # Step 5: Return the total number of 1 bits.
        return result

# Time Complexity:
# O(1), because the loop always runs 32 times, regardless of the size of `n`.
# Checking each bit of the 32-bit integer takes constant time.

# Space Complexity:
# O(1), as we only use a constant amount of space (the variable `result`).

# Solution 2: Bitmask II
class Solution2:
    def hammingWeight(self, n: int) -> int:
        # Step 1: Initialize the result variable to 0
        # This will store the number of 1 bits in the binary representation of `n`.
        result = 0

        # Step 2: Loop until `n` becomes 0
        # We continue checking each bit of `n` from the least significant bit (rightmost) to the most significant bit.
        while n:
            # Step 3: If the least significant bit is 1, increment the result counter
            # We use the bitwise AND operation with 1 (`n & 1`) to check if the least significant bit is 1.
            # If it is, increment `result` by 1.
            result += 1 if n & 1 else 0

            # Step 4: Right shift `n` to check the next bit
            # We perform a right shift on `n` (`n >>= 1`) to move to the next bit.
            n >>= 1

        # Step 5: Return the total number of 1 bits
        return result

# Time Complexity:
# O(k), where k is the number of bits in the binary representation of `n`.
# In the worst case, the loop runs for all the bits of `n`. If `n` is a 32-bit integer, the loop will run at most 32 times.

# Space Complexity:
# O(1), as we only use a constant amount of space (the variable `result`).

# Solution 3: Bitmask(Optimal)
class Solution3:
    def hammingWeight(self, n: int) -> int:
        # Step 1: Initialize the result variable to 0
        # This will store the number of 1 bits in the binary representation of `n`.
        result = 0

        # Step 2: Loop until `n` becomes 0
        # We continue to remove the least significant 1 bit from `n` until it becomes 0.
        while n:
            # Step 3: Apply the formula `n &= n - 1` to remove the least significant 1 bit.
            # The expression `n & (n - 1)` clears the rightmost 1 bit in `n`.
            # This operation reduces the number of 1 bits in `n` by 1 in each iteration.
            n &= n - 1

            # Step 4: Increment the result counter
            # Each time a 1 bit is cleared, increment the result counter.
            result += 1

        # Step 5: Return the total number of 1 bits
        return result

# Time Complexity:
# O(k), where k is the number of 1 bits in the binary representation of `n`.
# Each iteration of the loop clears one bit, so the loop runs for the number of 1 bits in `n`.

# Space Complexity:
# O(1), as we only use a constant amount of space (the variable `result`).

# Test cases
n1 = 0b00000000000000000000000000001011  # Binary: 1011, 3 ones
n2 = 0b00000000000000000000000000000000  # Binary: 0, no ones
n3 = 0b11111111111111111111111111111111  # Binary: all ones
n4 = 0b10000000000000000000000000000000  # Binary: single 1 bit
n5 = 0b00000000000000000000000010000000  # Binary: single 1 bit


# Testing Solution 1
solution1 = Solution1()
print(solution1.hammingWeight(n1))  # Expected output: 3
print(solution1.hammingWeight(n2))  # Expected output: 0
print(solution1.hammingWeight(n3))  # Expected output: 32
print(solution1.hammingWeight(n4))  # Expected output: 1
print(solution1.hammingWeight(n5))  # Expected output: 1


# Testing Solution 2
solution2 = Solution2()
print(solution2.hammingWeight(n1))  # Expected output: 3
print(solution2.hammingWeight(n2))  # Expected output: 0
print(solution2.hammingWeight(n3))  # Expected output: 32
print(solution2.hammingWeight(n4))  # Expected output: 1
print(solution2.hammingWeight(n5))  # Expected output: 1


# Testing Solution 3
solution3 = Solution3()
print(solution3.hammingWeight(n1))  # Expected output: 3
print(solution3.hammingWeight(n2))  # Expected output: 0
print(solution3.hammingWeight(n3))  # Expected output: 32
print(solution3.hammingWeight(n4))  # Expected output: 1
print(solution3.hammingWeight(n5))  # Expected output: 1