"""
Google

Longest Consecutive Sequence

Medium

Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. 
The elements do not have to be consecutive in the original array.
You must write an algorithm that runs in O(number) time.

Example 1:
Input: nums = [2,20,4,10,3,4,5]
Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:
Input: nums = [0,3,2,5,4,6,1,1]
Output: 7
"""

# Solution 1: Hashset
class Solution1:
    def longestConsecutive1(self, nums: list[int]) -> int:
        # Convert the list 'nums' to a set 'num_set' to allow O(1) time complexity for checking the presence of elements. 
        # This step ensures that we can quickly determine if a number is part of the sequence.
        num_set = set(nums)
        # Initialize a variable 'longest' to keep track of the length of the longest consecutive sequence found so far. Set it to 0 initially.
        longest = 0
        # Iterate through each 'number' in the list 'nums'.
        for number in nums:
            # For each number 'number', check if 'number' - 1 is not in 'num_set'. 
            # This check determines if 'number' is the start of a new sequence. 
            # If 'number - 1' is not present, it means 'number' is the smallest number in the current sequence.
            if (number - 1) not in num_set:
                # If 'number' is the start of a new sequence, initialize a variable length to 1. 
                # This variable will keep track of the length of the current sequence starting with 'number'.
                current_length = 1
                # Use a while loop to extend the current sequence. While 'number + current_length' is present in 'num_set', increment 'current_length'. 
                # This loop continues until the next consecutive number is not found in the set, indicating the end of the current sequence.
                while (number + current_length) in num_set:
                    current_length += 1
                # After determining the current_length of the current sequence, update 'longest' by taking the maximum of 'longest' and 'current_length'. 
                # This ensures that 'longest' always holds the current_length of the longest consecutive sequence found so far.
                longest = max(longest, current_length)
        # After iterating through all numbers in the list, return 'longest', which now holds the length of the longest consecutive sequence.
        return longest

# Time Complexity: 
# O(n) because worst case, for all the elements in 'nums' the longest sequence is 1

# Space Complexity: 
# O(n), where n is the number of elements in the input array

# Test cases
test_cases1 = [
    ([100, 4, 200, 1, 3, 2], 4),  # longest consecutive sequence: [1, 2, 3, 4]
    ([10, 20, 30, 40], 1),        # no consecutive numbers
    ([1, 2, 3, 4, 5], 5),         # entire array is a consecutive sequence
    ([7, 7, 7, 7, 7], 1),         # all elements are the same
    ([-1, 0, 1, 2, 3], 5),        # negative numbers included
    ([100, 4, 200, 1, 3, 2, 5], 5),  # longest consecutive sequence: [1, 2, 3, 4, 5]
    (list(range(100000, 1000000)), 900000),  # large input, sequence of 900,000 elements
    ([42], 1),                    # only one element
    ([10, 50], 1),                # no consecutive sequence
    ([-10, -5, -3, -1, -4], 3),   # longest consecutive sequence: [-5, -4, -3]
    ([1, 1000, 10000, 100000, 1000000], 1),  # no consecutive numbers
    ([9, 1, 4, 7, 3, 10, 2, 8, 6, 5], 10),  # longest consecutive sequence: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ([], 0),                      # empty array
    ([10], 1),                    # single element
    ([1, 2, 3, 10, 11, 12], 3)    # two consecutive sequences: [1, 2, 3] and [10, 11, 12]
]

# Run test cases
from collections import defaultdict
solution1 = Solution1()
for i, (nums, expected) in enumerate(test_cases1):
    result = solution1.longestConsecutive1(nums)
    print(f"Test Case {i + 1}: {'Pass' if result == expected else 'Fail'} (Expected {expected}, Got {result})")

# Solution 2: Hashmap
class Solution2:
    def longestConsecutive2(self, nums: list[int]) -> int:
        # Initialize a default-dictionary to store sequence length of each number.
        hashmap = defaultdict(int)
        # Initialize a variable to keep track of longest sequence.
        result = 0
        # Iterate through each 'number' in the list 'nums'
        for number in nums:
            # If the number is not part of any sequence (it's not in the hashmap)
            if not hashmap[number]:
                # Update the hashmap:
                # hashmap[number] stores the length of the consecutive sequence
                # that includes the current number 'number'. 
                hashmap[number] = hashmap[number - 1] + hashmap[number + 1] + 1
                # Now, we want to "merge" the two consecutive sequences
                # (one before 'number' and one after 'number') into a single larger sequence.
                # So, we update the boundaries of the sequences:
                hashmap[number - hashmap[number - 1]] = hashmap[number]
                hashmap[number + hashmap[number + 1]] = hashmap[number]
                # Update the result with the maximum length found so far
                result = max(result, hashmap[number])
        return result

# Time Complexity: 
# O(n) because worst case, for all the elements in 'nums' the longest sequence is 1

# Space Complexity: 
# O(n), where n is the number of elements in the input array

# Test cases
test_cases2 = [
    ([100, 4, 200, 1, 3, 2], 4),  # longest consecutive sequence: [1, 2, 3, 4]
    ([10, 20, 30, 40], 1),        # no consecutive numbers
    ([1, 2, 3, 4, 5], 5),         # entire array is a consecutive sequence
    ([7, 7, 7, 7, 7], 1),         # all elements are the same
    ([-1, 0, 1, 2, 3], 5),        # negative numbers included
    ([100, 4, 200, 1, 3, 2, 5], 5),  # longest consecutive sequence: [1, 2, 3, 4, 5]
    (list(range(100000, 1000000)), 900000),  # large input, sequence of 900,000 elements
    ([42], 1),                    # only one element
    ([10, 50], 1),                # no consecutive sequence
    ([-10, -5, -3, -1, -4], 3),   # longest consecutive sequence: [-5, -4, -3]
    ([1, 1000, 10000, 100000, 1000000], 1),  # no consecutive numbers
    ([9, 1, 4, 7, 3, 10, 2, 8, 6, 5], 10),  # longest consecutive sequence: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ([], 0),                      # empty array
    ([10], 1),                    # single element
    ([1, 2, 3, 10, 11, 12], 3)    # two consecutive sequences: [1, 2, 3] and [10, 11, 12]
]

# Run test cases
solution2 = Solution2()
for i, (nums, expected) in enumerate(test_cases2):
    result = solution2.longestConsecutive2(nums)
    print(f"Test Case {i + 1}: {'Pass' if result == expected else 'Fail'} (Expected {expected}, Got {result})")