"""
1793. Maximum Score of a Good Subarray

Hard

You are given an array of integers nums (0-indexed) and an integer k.
The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j.
Return the maximum possible score of a good subarray.

Example 1:
Input: nums = [1,4,3,7,4,5], k = 3
Output: 15
Explanation: The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15. 

Example 2:
Input: nums = [5,5,4,5,4,1,1,1], k = 0
Output: 20
Explanation: The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20.
"""

class Solution:
    # This function calculates the maximum score that can be achieved.
    def maximumScore(self, nums: list[int], k: int) -> int:
        # Initialize two pointers, left and right, at the kth index.
        left = right = k
        # Initialize the minimum score and maximum score with the value at the kth index.
        minimum_value = max_score = nums[k]
        
        # Continue the loop until the left pointer is within the bounds of the list 
        # or the right pointer is within the bounds of the list.
        while left >= 0 or right < len(nums):
            # Move the left pointer to the left as long as the value at the left pointer 
            # is greater than or equal to the minimum score.
            while left >= 0 and nums[left] >= minimum_value:
                left -= 1
            # Move the right pointer to the right as long as the value at the right pointer 
            # is greater than or equal to the minimum score.
            while right < len(nums) and nums[right] >= minimum_value:
                right += 1
            
            # Update the maximum score with the maximum of the current maximum score 
            # and the product of the length of the current subarray and the minimum score.
            score = ((right - left - 1) * minimum_value)
            if score > max_score:
                max_score = score  
            else:
                max_score = max_score

            # Update the minimum score based on the values at the left and right pointers.
            if left >= 0 and right < len(nums):
                # If both pointers are within bounds, update the minimum score with the maximum 
                # of the values at the left and right pointers.
                minimum_value = max(nums[left], nums[right])  # corrected line
            elif left >= 0:
                # If only the left pointer is within bounds, update the minimum score with the value at the left pointer.
                minimum_value = nums[left]
            elif right < len(nums):
                # If only the right pointer is within bounds, update the minimum score with the value at the right pointer.
                minimum_value = nums[right]
            else:
                # If neither pointer is within bounds, break the loop.
                break 
        # Return the maximum score.
        return max_score

test_cases = [
    ([_ for _ in range(0, 22, 3)], 3, 45),
    ([_ for _ in range(0, 100, 5)], 10, 500),
    ([1,4,3,7,4,5], 3, 15),
    ([5,5,4,5,4,1,1,1], 0, 20),
    ([1,2,3,4,5,6,7,1,2], 4, 16),
    ([1,1,1,7,2,2,1,1,0], 6, 8)
]
solution = Solution()
for idx, (numbers, k, expected) in enumerate(test_cases):
    result = solution.maximumScore(numbers, k)
    print(f"Test Case {idx + 1}: {'Pass' if result == expected else 'Fail'} (Expected {expected}, Got {result})")    