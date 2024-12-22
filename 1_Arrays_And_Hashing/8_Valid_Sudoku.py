"""
Valid Sudoku

Medium

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:
    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
"""

# class Solution:
#     def isValidSudoku(self, board: list[list[str]]) -> bool:
#         cols = defaultdict(set)
#         rows = defaultdict(set)
#         squares = defaultdict(set)  

#         for r in range(9):
#             for c in range(9):
#                 if board[r][c] == ".":
#                     continue
#                 if ( board[r][c] in rows[r]
#                     or board[r][c] in cols[c]
#                     or board[r][c] in squares[(r // 3, c // 3)]):
#                     return False

#                 cols[c].add(board[r][c])
#                 rows[r].add(board[r][c])
#                 squares[(r // 3, c // 3)].add(board[r][c])

#         return True

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Arrays to keep track of used numbers for each row, column, and box
        rows = [0] * 9      # 9 rows, each holding a bitmask of used numbers
        columns = [0] * 9   # 9 columns, each holding a bitmask of used numbers
        boxes = [0] * 9     # 9 sub-boxes (3x3), each holding a bitmask of used numbers
        
        # Traverse through each cell of the board
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue  # Skip empty cells
                ##DEBUG
                ##DEBUG
                ##DEBUG
                ##DEBUG
                ##DEBUG
                ##DEBUG
                ##DEBUG
                num = ord(board[i][j]) - ord('1')  # Convert '1'-'9' to 0-8
                mask = 1 << num                    # Create bitmask for the number
                box_index = (i // 3) * 3 + (j // 3)  # Calculate the index for the 3x3 sub-box
                
                # Check if the number is already present in the row, column, or box
                if (rows[i] & mask) or (columns[j] & mask) or (boxes[box_index] & mask):
                    return False  # If it exists, the Sudoku is invalid
                
                # Mark the number as used in the row, column, and box by setting the corresponding bit
                rows[i] |= mask
                columns[j] |= mask
                boxes[box_index] |= mask
        
        # If we successfully checked all the cells, return True (the board is valid)
        return True

# Time Complexity:
# O(1) because the board is 9 x 9

board1 = [
    ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
    ["2", ".", ".", "1", "9", "5", ".", ".", "."],
    ["3", "9", "8", ".", ".", ".", ".", "6", "."],
    ["4", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["5", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["6", ".", ".", ".", "2", ".", ".", ".", "6"],
    ["7", "6", ".", ".", ".", ".", "2", "9", "."],
    ["8", ".", ".", ".", "1", "9", ".", ".", "5"],
    ["9", ".", ".", ".", "8", ".", ".", "7", "1"]
]

solution = Solution()
print(solution.isValidSudoku(board1))  # Expected output: True
