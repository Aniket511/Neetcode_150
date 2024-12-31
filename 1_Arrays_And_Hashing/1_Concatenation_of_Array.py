"""
Concatenation of Array

Easy

Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
Specifically, ans is the concatenation of two nums arrays.
Return the array ans.

Example 1:
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]

Example 2:
Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]
"""

# Solution: Single Pass
class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        # Initialize a list 'ans' twice the length of 'nums' and set all values in it to zero
        ans = [0] * 2 * len(nums)
        # Iterate through all the values in nums using their index
        # for idx, val in enumerate(nums):
            # ans[idx] = ans[idx + len(nums)] = val
        for idx in range(len(nums)):
            # Change the value in 'ans' corresponding to value in 'nums' and the value in (current index + length of nums) i.e., ans[1] = ans[1 + len(nums)] = ans[1]  
            ans[idx] = ans[idx + len(nums)] = nums[idx]
        # After Iterating through all the values in 'nums' return the list 'ans'
        return ans

# Time Complexity: O(n)
# The time complexity of the provided solution is O(n), where n is the length of the input list `nums`. 
# This is because the solution iterates through the list `nums` once, performing constant-time operations for each element.

# Space Complexity: O(n)
# The space complexity is also O(n), as the solution creates a new list `ans` that is twice the size of `nums`. 
# This means that the space used grows linearly with the size of the input list. 

# Test Cases
test_cases = [
    ([1, 2, 3, 4], [1, 2, 3, 4, 1, 2, 3, 4]),
    ([4, 3, 2, 1, 2], [4, 3, 2, 1, 2, 4, 3, 2, 1, 2]),
    ([_ for _ in range(-100,101)] + [-23], 2 * ([_ for _ in range(-100,101)] + [-23])),
    ([2], [2, 2]),
    ([2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),
    ([1,1,1,3,3,4,3,2,4,2], [1, 1, 1, 3, 3, 4, 3, 2, 4, 2, 1 ,1 ,1 ,3 ,3 ,4 ,3 ,2 ,4 ,2])
]

solution = Solution()
for idx, (nums, expected) in enumerate(test_cases):
    result = solution.getConcatenation(nums)
    print(f"Test Case {idx + 1}: {'Pass' if result == expected else 'Fail'} (Expected {expected}, Got {result})")           