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
        triplets = []  # To store the resulting triplets
        nums.sort()  # Sorting the array to facilitate two-pointer approach

        # Loop through each element, considering it as the first element of the triplet
        for idx, val in enumerate(nums):
            # If the current value is greater than 0, break early because there can't be a sum of 0 with positive values
            if val > 0:
                break

            # Skip duplicates for the first element of the triplet to avoid repeating results
            if idx > 0 and val == nums[idx - 1]:
                continue

            # Two pointers: one starting just after the current element, and one at the end of the list
            left, right = idx + 1, len(nums) - 1
            while left < right:
                # Calculate the sum of the current triplet
                threeSum = val + nums[left] + nums[right]
                
                # If the sum is greater than 0, move the right pointer to the left to decrease the sum
                if threeSum > 0:
                    right -= 1
                # If the sum is less than 0, move the left pointer to the right to increase the sum
                elif threeSum < 0:
                    left += 1
                # If the sum is exactly 0, we've found a valid triplet
                else:
                    triplets.append([val, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Skip duplicate values for the 'left' pointer to avoid repeating results
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