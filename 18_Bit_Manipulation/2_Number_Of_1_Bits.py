"""
Amazon

Number of 1 Bits

Easy

Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).
(Return the number of 1 bits in its binary representation.)

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

# Solution 2: Bitmask (Optimal)
class Solution2:
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
# O(1), because the loop always runs 32 times, regardless of the size of `n`.
# Checking each bit of the 32-bit integer takes constant time.

# Space Complexity:
# O(1), as we only use a constant amount of space (the variable `result`).

# Test cases
test_cases = [
    (0b00000000000000000000000000001011, 3),    # Binary: 1011, 3 ones
    (0b00000000000000000000000000000000, 0),    # Binary: 0, no ones
    (0b11111111111111111111111111111111, 32),   # Binary: all ones
    (0b10000000000000000000000000000000, 1),    # Binary: single 1 bit
    (0b00000000000000000000000010000000, 1)     # Binary: single 1 bit
]

solution1 = Solution1()
for i, (nums, expected) in enumerate(test_cases):
    result = solution1.hammingWeight(nums)
    print(f"Test Case {i + 1}: {'Pass' if result == expected else 'Fail'} (Expected {expected}, Got {result})")

solution2 = Solution2()
for i, (nums, expected) in enumerate(test_cases):
    result = solution2.hammingWeight(nums)
    print(f"Test Case {i + 1}: {'Pass' if result == expected else 'Fail'} (Expected {expected}, Got {result})")