"""
Top K Frequent Elements

Medium

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order. 

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Initialize a list `frequency` where each index represents a frequency.
        frequency = [[] for _ in range(len(nums) + 1)]

        # Step 2: Count the frequencies of each number in `nums`.
        count = {}
        for number in nums:
            count[number] = 1 + count.get(number, 0)

        # Step 3: Fill the `frequency` list based on the frequencies.
        for number, cnt in count.items():
            frequency[cnt].append(number)

        # Step 4: Collect the top k frequent elements from `frequency`.
        result = []
        # Traverse `frequency` starting from the highest frequency to get the top k elements.
        for idx in range(len(frequency) - 1, 0, -1):
            for number in frequency[idx]:
                result.append(number)
                if len(result) == k:
                    return result

# Test cases to validate the solution
test_cases = [
    ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
    ([1, 1, 1, 1], 1, [1]),
    ([4, 4, 5, 5, 6, 6], 2, [4, 5]),  # Order can vary
    ([1, 2, 2, 3, 3, 3, 4, 5], 3, [3, 2, 1]),  # Order can vary
    ([-1, -1, 2, 3, 2, 2, -1, 3, 3], 2, [3, 2]),  # Order can vary
    ([1], 1, [1]),
    ([5, 5, 5, 5, 5, 5], 1, [5]),
    ([1, 2, 2, 3], 5, [2, 3, 1]),  # Should return all elements as there are not enough unique numbers
    ([idx for idx in range(1, 1000001)] + [999999, 999998, 999997], 3, [999999, 999998, 999997])
]

solution = Solution()
print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))     