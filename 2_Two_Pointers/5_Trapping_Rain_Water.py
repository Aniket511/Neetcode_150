"""
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

class Solution:
    def trap(self, height: list[int]) -> int:
        # Initialize pointers
        left = 0                # Pointer at the beginning of the array (leftmost bar)
        right = len(height) - 1  # Pointer at the end of the array (rightmost bar)
        # Initialize variables to keep track of the maximum heights encountered
        left_max = 0            # Maximum height seen from the left side
        right_max = 0           # Maximum height seen from the right side
        # This variable will accumulate the total amount of water trapped
        trapped_water = 0
        # While the left pointer does not surpass the right pointer
        while left <= right:
            # We process the bar at the left pointer if its height is less than or equal to the bar at the right pointer
            if height[left] <= height[right]:
                # If the current height at left is greater than or equal to the left_max, we update left_max
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    # If the current height at left is smaller than left_max, calculate trapped water
                    trapped_water += left_max - height[left]
                # Move the left pointer to the right to process the next bar
                left += 1
            else:
                # If the height at right is smaller, process the bar at the right pointer
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    # If the current height at right is smaller than right_max, calculate trapped water
                    trapped_water += right_max - height[right]
                # Move the right pointer to the left to process the next bar
                right -= 1
        # Return the total amount of water trapped
        return trapped_water