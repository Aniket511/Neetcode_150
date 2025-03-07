"""
Number of Submatrices That Sum to Target

Hard

Given a matrix and a target, return the number of non-empty submatrices that sum to target.
A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.
Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

Example 1:
Input: matrix = [
                [0,1,0],
                [1,1,1],
                [0,1,0]], 
target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.

Example 2:
Input: matrix = [[1,-1],
                [-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.

Example 3:
Input: matrix = [[904]], target = 0
Output: 0
"""

class Solution():
    def numSubmatrixSumTarget(self, matrix, target):
        rows, columns = len(matrix), len(matrix[0])
        prefix_sum = [[0] * (columns + 1) for _ in range(rows + 1)]

        # Compute the 2D prefix sum
        for row in range(1, rows + 1):
            for col in range(1, columns + 1):
                prefix_sum[row][col] = matrix[row - 1][col - 1] + prefix_sum[row - 1][col] + prefix_sum[row][col - 1] - prefix_sum[row - 1][col - 1]

        count = 0

        # Iterate through all possible pairs of columns
        for col1 in range(1, columns + 1):
            for col2 in range(col1, columns + 1):
                # Use a hashmap to count the number of subarrays with a given sum
                prefix_sum_map = {0: 1}
                current_sum = 0
                for row in range(1, rows + 1):
                    current_sum = prefix_sum[row][col2] - prefix_sum[row][col1 - 1]
                    if current_sum - target in prefix_sum_map:
                        count += prefix_sum_map[current_sum - target]
                    if current_sum in prefix_sum_map:
                        prefix_sum_map[current_sum] += 1
                    else:
                        prefix_sum_map[current_sum] = 1

        return count

test_cases = [
    ([[0,1,0],[1,1,1],[0,1,0]], 0, 4),
    ([[1,-1],[-1,1]], 0 , 5),
    ([[904]], 0, 0),
    ([[904,1,0],[1,1,1],[0,1,0]], 0, 3),
    ([[0,0,0,1,1],[1,1,1,0,1],[1,1,1,1,0],[0,0,0,1,0],[0,0,0,1,1]], 0, 28)
]

solution = Solution()
for idx, (nums, target, expected) in enumerate(test_cases):
    result = solution.numSubmatrixSumTarget(nums, target)
    print(f"Test Case {idx + 1}: {'Pass' if result == expected else 'Fail'} (Expected {expected}, Got {result})")     