"""
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

#Solution: Three Pointer
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Step 1: Check if the list has fewer than 3 elements. If so, return an empty list
        if len(nums) < 3:
            return []

        # Step 2: Sort the list. Sorting helps to efficiently find pairs using two-pointer technique.
        nums.sort()

        # Step 3: Early exit optimization
        # If the largest element is less than 0 or the smallest element is greater than 0,
        # there's no way to get a sum of 0 because we can't form a zero-sum with only positive or negative numbers.
        if (nums[-1] < 0) or (nums[0] > 0):
            return []

        # Step 4: Initialize an empty list to store the triplets
        triplets = []

        # Step 5: Loop through the list using `left` as the first pointer. We stop at len(nums) - 2 because we need at least two more elements to form a triplet.
        for left in range(len(nums) - 2):
            # Step 6: Skip the same element to avoid duplicate triplets. This ensures that each triplet is unique.
            if left > 0 and nums[left] == nums[left - 1]:
                continue

            # Step 7: If the current element (nums[left]) is greater than 0, we can break the loop early.
            # Since the array is sorted, all subsequent elements will be positive, and we can't form zero-sum triplets with positive numbers.
            elif nums[left] > 0:
                break

            # Step 8: Initialize two pointers, `middle` and `right`, to look for pairs that sum to the negation of nums[left]
            else:
                target = -nums[left]
                middle = left + 1
                right = len(nums) - 1

                # Step 9: Use the two-pointer technique to find pairs (nums[middle], nums[right]) that sum to `target`.
                while middle < right:
                    total = nums[middle] + nums[right]

                    # Step 10: If the sum of the pair is less than the target, move the `middle` pointer to the right to increase the sum.
                    if total < target:
                        middle += 1

                    # Step 11: If the sum of the pair is greater than the target, move the `right` pointer to the left to decrease the sum.
                    elif total > target:
                        right -= 1

                    # Step 12: If the sum is equal to the target, we have found a valid triplet.
                    else:
                        # Add the triplet [nums[left], nums[middle], nums[right]] to the result list.
                        triplets.append([nums[left], nums[middle], nums[right]])

                        # Step 13: Move both pointers to avoid duplicate pairs.
                        middle += 1
                        right -= 1

                        # Step 14: Skip duplicate elements at the `middle` pointer by moving it to the next unique number.
                        while middle < right and nums[middle] == nums[middle - 1]:
                            middle += 1

        # Step 15: Return the list of unique triplets that sum to zero.
        return triplets

# Time Complexity: O(n^2)
# The time complexity of the provided `threeSum` function is O(n^2), where n is the number of elements in the input list `nums`. 
# This is because the function sorts the list initially, which takes O(n log n) time, and then it uses a nested loop structure: 
# the outer loop iterates through each element (O(n)), and for each element, the inner while loop performs a two-pointer search, which also runs in O(n) in the worst case. 
# Therefore, the overall time complexity is dominated by the O(n^2) term from the nested loops.

# Space Complexity: O(k) or O(1)
# The space complexity of the function is O(1) if we disregard the space used for the output. 
# The function uses a constant amount of extra space for variables like `left`, `middle`, `right`, and `total`. 
# However, the space complexity can be considered O(k) where k is the number of triplets found, due to the storage of the resulting triplets in the `triplets` list. 
# In the worst case, if all combinations are valid triplets, this could approach O(n) in terms of the number of triplets stored.

test_cases = [
    ([1, -2, 3, -4, 1, 2, -3, 4], [[-4, 1, 3], [-3, 1, 2], [-2, 1, 1]]),
    ([4, -3, 2, -1, 2, -4, 3, -2, 1, 2], [[-4, 1, 3], [-4, 2, 2], [-3, -1, 4], [-3, 1, 2], [-2, -1, 3]]),
    ([_ for _ in range(-10,11)] + [-23],
    [[-10, 0, 10], [-10, 1, 9], [-10, 2, 8], [-10, 3, 7], [-10, 4, 6], [-9, -1, 10], [-9, 0, 9], [-9, 1, 8], 
    [-9, 2, 7], [-9, 3, 6], [-9, 4, 5], [-8, -2, 10], [-8, -1, 9], [-8, 0, 8], [-8, 1, 7], [-8, 2, 6], [-8, 3, 5], [-7, -3, 10], [-7, -2, 9], [-7, -1, 8], 
    [-7, 0, 7], [-7, 1, 6], [-7, 2, 5], [-7, 3, 4], [-6, -4, 10], [-6, -3, 9], [-6, -2, 8], [-6, -1, 7], [-6, 0, 6], [-6, 1, 5], [-6, 2, 4], [-5, -4, 9], 
    [-5, -3, 8], [-5, -2, 7], [-5, -1, 6], [-5, 0, 5], [-5, 1, 4], [-5, 2, 3], [-4, -3, 7], [-4, -2, 6], [-4, -1, 5], [-4, 0, 4], [-4, 1, 3], [-3, -2, 5], 
    [-3, -1, 4], [-3, 0, 3], [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]),
    ([2], []),
    ([2, 0, -2, 0, -2, -3, -4, -5, -1, -2, -3, -9, -8, -7, -1, -2, 3, 5, 4, 7, 9, 8, 6, 5, 2, 1, 4, 3, 5, 8, 6], 
    [[-9, 0, 9], [-9, 1, 8], [-9, 2, 7], [-9, 3, 6], [-9, 4, 5], [-8, -1, 9], [-8, 0, 8], [-8, 1, 7], [-8, 2, 6], [-8, 3, 5], [-8, 4, 4], 
    [-7, -2, 9], [-7, -1, 8], [-7, 0, 7], [-7, 1, 6], [-7, 2, 5], [-7, 3, 4], [-5, -4, 9], [-5, -3, 8], [-5, -2, 7], [-5, -1, 6], [-5, 0, 5], 
    [-5, 1, 4], [-5, 2, 3], [-4, -3, 7], [-4, -2, 6], [-4, -1, 5], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-3, -3, 6], [-3, -2, 5], [-3, -1, 4], 
    [-3, 0, 3], [-3, 1, 2], [-2, -2, 4], [-2, -1, 3], [-2, 0, 2], [-1, -1, 2], [-1, 0, 1]]),
    ([1, 1, -1, 3, 3, -4, 3, 2, -4, 2, -1 ,1 ,-1 ,3 ,-3 ,4 ,3 ,-2 ,4 ,2], [[-4, 1, 3], [-4, 2, 2], [-3, -1, 4], [-3, 1, 2], [-2, -1, 3], [-2, 1, 1], [-1, -1, 2]])
]

solution = Solution()
for idx, (nums, expected) in enumerate(test_cases):
    result = solution.threeSum(nums)
    print(f"Test Case {idx + 1}: {'Pass' if result == expected else 'Fail'} (Expected {expected}, Got {result})")    