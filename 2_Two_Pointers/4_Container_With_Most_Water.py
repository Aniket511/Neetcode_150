"""
Google, Facebook

Container With Most Water

Medium

You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Initialize the variable to store the maximum area
        max_area = 0      
        # Left pointer starts at the beginning of the list          
        left = 0         
        # Right pointer starts at the end of the list            
        right = len(height) - 1      
        # Loop until left pointer is not equal to or exceeds the right pointer
        while left < right:
            # Calculate the area with the current left and right pointers
            current_area = (right - left) * min(height[left], height[right])
            # Update the maximum area found so far
            max_area = max(max_area, current_area)
            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1        
        # Return the maximum area found
        return max_area

# Time Complexity: 
# O(n), where n is the number of elements in the height array. 
# This is because the left and right pointers each move at most n times, and for each movement, 
# you are performing constant-time operations (i.e., calculating the area and comparing values).

# Space Complexity: 
# O(1), since the algorithm uses a constant amount of extra space. 
# The input height array is not modified, and no additional space is allocated for auxiliary structures.

# Test Cases
test_cases = [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1),
    ([1,7,2,5,4,7,3,6], 36),
    ([2, 2, 2], 4),
]

solution = Solution()
for i, (nums, expected) in enumerate(test_cases):
    result = solution.maxArea(nums)
    print(f"Test Case {i + 1}: {'Pass' if result == expected else 'Fail'} (Expected {expected}, Got {result})")