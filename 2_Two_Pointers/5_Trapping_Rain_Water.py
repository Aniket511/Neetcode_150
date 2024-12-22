"""
Google

Trapping Rain Water

Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
"""

# Solution: Two Pointer
class Solution:
    def trap(self, height: list[int]) -> int:
        # Edge case: If the input is empty, we return zero
        if not height: 
            return 0
        # Step 1: initialize pointer and variables
        # Initialize two pointers at the beginning and end of list 'height'
        left = 0
        right = len(height) - 1
        # Initialize variables left_max and right_max to store the maximum height encountered fron the left and right side respectively
        left_max = height[left]
        right_max = height[right]
        # Initialize a variable water to keep track of total traped water
        water = 0
        # Step 2: Loop until both points meet, i.e., continue looping while left pointer is less than right indicating there are still bar to process
        while left < right:
            # Step 3: Check which side to move
            # Compare left_max and right_max height
            # If left_max is less than right_max, move the left pointer to the right and update left_max
            if left_max < right_max:
                left += 1
                # Step 4: Calculate the traped water
                # Calculate the water traped at the current position based on the difference between the maximum height and the current height
                left_max = max(left_max, height[left])
                # Accumulate this water amount to the 'water' variable
                water += left_max - height[left]
            # If right_max is less than left_max, move the right pointer to the left and update right_max
            else:
                right -= 1
                # Calculate the water traped at the current position based on the difference between the maximum height and the current height
                right_max = max(right_max, height[right])
                # Accumulate this water amount to the 'water' variable
                water += right_max - height[right]
        # Step 5: Return total trapped water
        # After the loop ends, return the total trapped water accumulated in 'water' variable
        return water

# Time Complexity:
# O(n), because you only make a single pass through the array (with left and right pointers meeting in the middle). 
# The loop runs at most n times, where n is the length of the height list.

# Space Complexity:
# O(1) because, you only use a constant amount of extra space (left, right, left_max, right_max, and water), which doesn't depend on the size of the input.

# Test Cases:
test_cases = [
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    ([4, 2, 0, 3, 2, 5], 9),
    ([0, 2, 0, 3, 1, 0, 1, 3, 2, 1], 9),
    ([], 0),
    ([3, 2, 8, 2, 10], 7),
]

solution = Solution()
for i, (heights, expected) in enumerate(test_cases):
    result = solution.trap(heights)
    print(f"Test Case {i + 1}: {'Pass' if result == expected else 'Fail'} (Expected {expected}, Got {result})")