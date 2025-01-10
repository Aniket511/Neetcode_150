"""
Amazon

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

# Solution 1: Hashset (one pass)
from collections import defaultdict
class Solution1:
    def isValidSudoku1(self, board: list[list[str]]) -> bool:
        # Initialize dictionaries to keep track of numbers seen in columns, rows, and 3x3 subgrids.
        cols = defaultdict(set)     # A set to track numbers in each column
        rows = defaultdict(set)     # A set to track numbers in each row
        squares = defaultdict(set)  # A set to track numbers in each 3x3 subgrid
        
        # Iterate over each cell in the 9x9 Sudoku board.
        for r in range(9):
            for c in range(9):
                # If the current cell is empty (i.e., '.'), skip it.
                if board[r][c] == ".":
                    continue
                
                # Check if the current number already exists in the current row, column, or 3x3 subgrid.
                if (board[r][c] in rows[r]  # Check the row 'r'
                    or board[r][c] in cols[c]  # Check the column 'c'
                    or board[r][c] in squares[(r // 3, c // 3)]):  # Check the 3x3 subgrid
                    return False  # If the number exists in any of these, the board is invalid.

                # If no duplicates are found, add the current number to the respective sets
                cols[c].add(board[r][c])  # Add the number to the column 'c'
                rows[r].add(board[r][c])  # Add the number to the row 'r'
                squares[(r // 3, c // 3)].add(board[r][c])  # Add the number to the 3x3 subgrid

        return True  # If no invalid conditions are found, the Sudoku board is valid.

# Time Complexity:
# O(81) -> O(1) because the board size is constant rows(9) ∗ columns(9) = 81

# Space Complexity:
# O(243) -> O(1) because rows(81) + columns(81) + boxes(81) = 243

test_cases1 = [
    # Valid Sudoku board example
    (
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            ["9", ".", ".", ".", "8", ".", ".", "7", "9"]
        ],
        False
    ),
    # Board with duplicate in row
    (
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            ["9", "9", "8", ".", ".", ".", ".", "6", "."],  # Invalid row (duplicate "9")
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            ["9", ".", ".", ".", "8", ".", ".", "7", "9"]
        ],
        False
    ),
    # Board with valid numbers but incorrect grid placement
    (
        [
            ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ["2", "3", "4", "5", "6", "7", "8", "9", "1"],
            ["3", "4", "5", "6", "7", "8", "9", "1", "2"],
            ["4", "5", "6", "7", "8", "9", "1", "2", "3"],
            ["5", "6", "7", "8", "9", "1", "2", "3", "4"],
            ["6", "7", "8", "9", "1", "2", "3", "4", "5"],
            ["7", "8", "9", "1", "2", "3", "4", "5", "6"],
            ["8", "9", "1", "2", "3", "4", "5", "6", "7"],
            ["9", "1", "2", "3", "4", "5", "6", "7", "8"]
        ],
        False
    ),
    # An empty board (should be considered valid since no conflicts exist)
    (
        [
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."]
        ],
        True
    )
]

# Testing the Sudoku validation
solution1 = Solution1()
for i, (board, expected) in enumerate(test_cases1):
    result = solution1.isValidSudoku1(board)
    print(f"Test Case {i + 1}: {'Pass' if result == expected else 'Fail'} (Expected {expected}, Got {result})")


# Solution 2: Bitmask
class Solution2:
    def isValidSudoku2(self, board: list[list[str]]) -> bool:
        # Arrays to keep track of used numbers for each row, column, and box
        rows = [0] * 9      # 9 rows, each holding a bitmask of used numbers
        columns = [0] * 9   # 9 columns, each holding a bitmask of used numbers
        boxes = [0] * 9     # 9 sub-boxes (3x3), each holding a bitmask of used numbers
        
        # Traverse through each cell of the board
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue  # Skip empty cells
                # Convert '1'-'9' to 0-8 because bitwise operations, such as shifting bits, are easier to apply when the numbers start at 0
                num = int(board[i][j]) - 1 
                 # Create bitmask for the number
                mask = 1 << num     
                # Calculate the index for the 3x3 sub-box  
                # Multiplying (i // 3) by 3 and adding (j // 3) gives the unique index of the subgrid, ranging from 0 to 8            
                box_index = (i // 3) * 3 + (j // 3)  
                
                # Check if the number is already present in the row, column, or box
                if (rows[i] & mask) or (columns[j] & mask) or (boxes[box_index] & mask):
                    # If it exists, the Sudoku is invalid
                    return False  
                
                # Mark the number as used in the row, column, and box by setting the corresponding bit
                else:
                    rows[i] |= mask
                    columns[j] |= mask
                    boxes[box_index] |= mask
        
        # If we successfully checked all the cells, return True (the board is valid)
        return True

# Time Complexity:
# O(81) -> O(1) because the board size is constant rows(9) ∗ columns(9) = 81

# Space Complexity:
# O(27) -> O(1) because because the space used is fixed regardless of the input rows(9) + columns(99) + boxes(9) = 27

