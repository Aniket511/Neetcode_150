"""
Product of Array Except Self

Medium

Given an integer array nums, return an array answer such that answer[idx] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Initialize the output array with 1s. This will store the final result.
        # Each index will eventually store the product of all numbers except the current one.
        output = [1] * len(nums)
        
        # Step 1: Calculate the prefix product for each index.
        # 'prefix' will store the product of all numbers to the left of the current index.
        prefix = 1
        for i in range(len(nums)):
            # For each index, update the output array by multiplying with the current prefix product.
            output[i] *= prefix  # This is equivalent to setting output[i] to product of all elements before i
            prefix *= nums[i]  # Update the prefix to include the current element nums[i]
        
        # Step 2: Calculate the postfix product for each index.
        # 'postfix' will store the product of all numbers to the right of the current index.
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            # Multiply the current value in output with the postfix product.
            output[i] *= postfix  # This updates output[i] by including the product of elements after i.
            postfix *= nums[i]  # Update the postfix to include the current element nums[i]
    
        # The output array now contains the product of all elements except the current one for each index.
        return output
            
# Time Complexity:
# O(n) where n is the length of nums

# Space Complexity:
# O(1) since output array is excluded from the space analysis

test_cases = [
    ([1, 2, 3, 4], [24, 12, 8, 6]),
    ([0, 2, 3, 4], [24, 0, 0, 0]),
    ([1, 1, 1, 1], [1, 1, 1, 1]),
    ([5], [1]),
    ([-1, 2, -3, 4], [-24, 12, -8, 6]),
    ([1, 2, 3, -4], [-24, -12, -8, 6]),
    ([2, 4, 6, 8 ,10], [1920, 960, 640, 480, 384]),
    ([10] * 5, [10000] * 5),
]

# Initialize Solution class
solution = Solution()

# Running the test cases
for i, (nums, expected) in enumerate(test_cases):
    result = solution.productExceptSelf(nums)
    print(f"Test Case {i + 1}: {'Pass' if result == expected else 'Fail'} (Expected {expected}, Got {result})")