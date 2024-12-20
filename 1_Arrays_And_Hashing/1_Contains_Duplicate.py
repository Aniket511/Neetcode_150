"""
Microsoft 

Contains Duplicate

Easy

Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

# Solution 1: Set
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Step 1: Set Initialization
        # Initialize an empty set to store unique values as we iterate through the list.
        # A set is chosen because it provides average O(1) time complexity for both insertions and membership checks, 
        # which makes it efficient for checking duplicates.
        number_set = set()

        # Step 2: Iterate through the list
        for number in nums:
            # Check for duplicate
            if number in number_set:
                # If a duplicate is found, return True
                return True
            # Step 3: Add the number to the set if it is not already present
            number_set.add(number)
        
        # Step 4: Return False if all numbers in the list are distinct
        return False

# Time Complexity:
# O(n) because we need to iterate through the entire list once, where `n` is the length of the list.

# Space Complexity:
# O(n) because, in the worst case, we may need to store all the values of the list in the set.

# Test Cases:
test_cases = [
    ([1, 2, 3, 4], False),
    ([4, 3, 2, 1, 2], True),
    ([_ for _ in range(-100,101)] + [-23], True),
    ([2], False),
    ([2, 2, 2, 2, 2], True),
    ([1,1,1,3,3,4,3,2,4,2], True)
]

solution = Solution()
for i, (nums, expected) in enumerate(test_cases):
    result = solution.containsDuplicate(nums)
    print(f"Test Case {i + 1}: {'Pass' if result == expected else 'Fail'} (Expected {expected}, Got {result})")