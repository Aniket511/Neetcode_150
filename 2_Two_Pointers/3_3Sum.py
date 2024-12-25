"""
Facebook

3Sum

Medium

Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Step 1: Initialize an empty list 
        # Create an empty list 'triplets' to store the triplets whose sum is zero
        triplets = [] 
        # Step 2: Sort the input array
        # Sort the input array in an non-decreasing order to avoid duplicate triplets
        nums.sort()  
        # Step 3: Iterate through the list
        # Enumerate the list to get index of the values in nums
        for idx, val in enumerate(nums):
            # Since we sort the array in non-decreasing order, if the first element is positive, then the remaining elements will also be positive so we break the loop
            if val > 0:
                break
            # Step 4: Skip Duplicate Elements
            # Check if the current element is a duplicate of the previous element and skip if it is
            if idx > 0 and val == nums[idx - 1]:
                continue
            # Step 5: Initialize pointers
            # initialize pointers 'left' and 'right' to point to the elements next to the 'idx' of the current element and at the end of the array, respectively 
            left, right = idx + 1, len(nums) - 1
            # Step 6: Two pointer approach
            # Loop until left pointer is less than right pointer
            while left < right:
                # Step 7: Calculate total of current triplet
                threeSum = val + nums[left] + nums[right]
                # Step 8: Adjust pointer based on total
                # if the total is greater than zero, then we decrement the right pointer by one
                if threeSum > 0:
                    right -= 1
                # Else if the total is less than zero, then we increment the left pointer by one
                elif threeSum < 0:
                    left += 1
                # Else if the total sum equals zero, add the triplet values to the variable 'triplets'
                else:
                    triplets.append([val, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Step 9: Skipping duplicates on the left
                    # After finding a valid triplet, we skip any duplicate values on the left side to avoid duplicates 
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return triplets

# Time Complexity:
# Sorting: Sorting the array takes O(n log n), where n is the length of the input array.
# Two-pointer Traversal: For each element in the array (in the outer loop), we perform a two-pointer search, 
# which takes O(n) time. Thus, the overall time complexity for the two-pointer part is O(n²).
# Overall Time Complexity: The overall time complexity of the algorithm is O(n²) due to the two-pointer traversal combined with sorting.

# Space Complexity:
# Auxiliary Space: The space complexity is O(1) (excluding the space used to store the result),
# because we only use a few extra variables like idx, val, left, and right, and the space used to store the result list triplets.
# The space for triplets depends on the number of triplets found, but it is not counted in the auxiliary space complexity.

# Test Cases:
test_cases = [
    # Standard test cases
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),  # Multiple valid triplets
    ([0, 0, 0], [[0, 0, 0]]),  # Only one unique triplet
    ([1, 2, -2, -1], []),  # No valid triplet
    ([1, 1, -2], [[-2, 1, 1]]),  # Valid triplet with duplicates
    ([], []),  # Empty input list
    ([1, 2, 3], []),  # No valid triplet because no sum equals 0
    ([-1, -1, -1, 2], [[-1, -1, 2]])  # Unique triplet with duplicates
]

solution = Solution()

# Run the test cases
for idx, (nums, expected) in enumerate(test_cases):
    result = solution.threeSum(nums)
    print(f"Test Case {idx + 1}: {'Pass' if result == expected else 'Fail'} (Expected {expected}, Got {result})")