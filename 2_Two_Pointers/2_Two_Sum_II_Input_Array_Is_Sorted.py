"""
Amazon

Two Sum II - Input Array Is Sorted

Medium

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # Initialize two pointers, left starting at the beginning and right starting at the end of the list.
        left = 0
        right = len(numbers) - 1
        # Loop until the two pointers meet.
        while left < right:
            # Calculate the sum of the values at the two pointers.
            total = numbers[left] + numbers[right]
            # If the total equals the target, we have found the solution.
            if total == target:
                # Return the indices (1-based indexing).
                return [left + 1, right + 1]
            # If the total is greater than the target, move the right pointer left to reduce the sum.
            elif total > target:
                right -= 1
            # If the total is less than the target, move the left pointer right to increase the sum.
            else:
                left += 1

# Time Complexity: 
# O(n), The time complexity is linear because the algorithm makes a single pass through the list with two pointers. 
# Each pointer only moves once, and we do not have nested loops.

# Space Complexity:
# O(1), The algorithm only uses a constant amount of extra space, aside from the input list, which is not modified. 
# We're just using the two pointers (left and right).

# Test Cases:
test_cases = [
    ([-12, -4 , -2, 0], -14, [1, 3]),  # -12 + -2 = -14, expected output is [1, 3]
    ([1, 2, 3, 4, 5], 9, [4, 5]),  # 4 + 5 = 9, expected output is [4, 5]
    ([1, 3, 5, 7, 9], 8, [1, 4]),  # 1 + 7 = 8, expected output is [1, 4]
    ([0, 1, 2, 3, 4, 5, 6], 6, [1, 7]),  # 0 + 6 = 6, expected output is [1, 7]
    ([-1, 0], -1 ,[1, 2]),  # - 1 + 0 = -1, expected output is [1, 2]
    ([2, 3, 4], 6, [1, 3]),  # 2 + 4 = 6, expected output is [1, 3]
]

solution = Solution()

# Run the test cases
for i, (numbers, target, expected) in enumerate(test_cases):
    result = solution.twoSum(numbers, target)
    print(f"Test Case {i + 1}: {'Pass' if result == expected else 'Fail'} (Expected {expected}, Got {result})")