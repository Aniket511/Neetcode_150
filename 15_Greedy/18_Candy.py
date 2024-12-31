"""
Candy

Hard

There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
You are giving candies to these children subjected to the following requirements:
    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

Example 1:
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
"""

class Solution:
    def candy(self, ratings: list[int]) -> int:
        # Step 1: Initialize the total candies count with the number of children (minimum 1 candy each)
        total_candies = len(ratings)

        # Step 2: Initialize an idx variable to traverse through the ratings list
        idx = 1

        # Step 3: Loop through the ratings to calculate candies distribution
        while idx < len(ratings):
            # Case 1: If the current child's rating is equal to the previous child's rating,
            # no additional candies are given. Simply move to the next child.
            if ratings[idx] == ratings[idx - 1]:
                idx += 1
                continue
            
            # Step 4: Handle an "ascending slope" (ratings increasing):
            # Start counting candies for children with increasing ratings.
            current_peak_candies = 0
            while idx < len(ratings) and ratings[idx] > ratings[idx - 1]:
                current_peak_candies += 1
                total_candies += current_peak_candies
                idx += 1
            
            # If we reach the end of the list during the ascending slope, return the total candies.
            if idx == len(ratings):
                return total_candies

            # Step 5: Handle a "descending slope" (ratings decreasing):
            # Start counting candies for children with decreasing ratings.
            current_valley_candies = 0
            while idx < len(ratings) and ratings[idx] < ratings[idx - 1]:
                current_valley_candies += 1
                total_candies += current_valley_candies
                idx += 1

            # Step 6: Adjust for the peak shared between the ascending and descending slopes.
            # Subtract the smaller of the peak counts from the total, as the peak child was double-counted.
            total_candies -= min(current_peak_candies, current_valley_candies)

        # Step 7: Return the total candies after processing all children.
        return total_candies

# Test Cases
test_cases = [
    ([1, 2, 3, 4, 1], 11),
    ([4, 3, 2, 1, 2], 12),
    ([_ for _ in range(-100,101)] + [-23], 20302),
    ([2], 1),
    ([_ for _ in range(-100, 101)], 20302),
    ([2, 2, 2, 2, 2], 5),
    ([1,1,1,3,3,4,3,2,4,2], 15)
]

solution = Solution()
for idx, (nums, expected) in enumerate(test_cases):
    result = solution.candy(nums)
    print(f"Test Case {idx + 1}: {'Pass' if result == expected else 'Fail'} (Expected {expected}, Got {result})")     