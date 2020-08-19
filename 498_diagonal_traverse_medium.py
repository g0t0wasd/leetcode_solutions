class Solution:
    """
    Description:
        Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.
        Example:
        Input:
        [
         [ 1, 2, 3 ],
         [ 4, 5, 6 ],
         [ 7, 8, 9 ]
        ]

        Output:  [1,2,4,7,5,3,6,8,9]
    Idea:
        A - get all diagonals and flip the even ones
        B - simulate traversal with calculating new head every time
    Complexity:
        Time:
            A: O(m*n)
            B: O(m*n)
        Space:
            A: O(min(m,n))
            B: O(1)
    """
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
#         if not matrix or not matrix[0]:
#             return []
#         width = len(matrix[0])
#         height = len(matrix)
        
#         result = []
#         for d in range(width + height -1):
#             intermediate = []
#             if d < width:
#                 row = 0
#                 col = d
#             else:
#                 row = d - width + 1
#                 col = width - 1
#             while row < height and col > -1:
#                 intermediate.append(matrix[row][col])
#                 row += 1
#                 col -= 1
#             if d % 2 != 0:
#                 result.extend(intermediate)
#             else:
#                 result.extend(intermediate[::-1])            
#         return result
        # Check for an empty matrix
        if not matrix or not matrix[0]:
            return []
        N, M = len(matrix), len(matrix[0])
        row, col = 0, 0
        direction = 1
        result = []
        while row < N and col < M:
            result.append(matrix[row][col])
            # Move along in the current diagonal depending upon
            # the current direction.[i, j] -> [i - 1, j + 1] if
            # going up and [i, j] -> [i + 1][j - 1] if going down.
            if direction == 1:
                new_row = row - 1
                new_col = col + 1
            else:
                new_row = row + 1
                new_col = col - 1
            # Checking if the next element in the diagonal is within the
            # bounds of the matrix or not. If it's not within the bounds,
            # we have to find the next head.
            if new_row < 0 or new_row == N or new_col < 0 or new_col == M:
                # If the current diagonal was going in the upwards
                # direction.
                if direction:
                    # For an upwards going diagonal having [i, j] as its tail
                    # If [i, j + 1] is within bounds, then it becomes
                    # the next head. Otherwise, the element directly below
                    # i.e. the element [i + 1, j] becomes the next head
                    if col == M - 1:
                        row += 1
                    if col < M - 1:
                        col += 1
                else:
                    # For a downwards going diagonal having [i, j] as its tail
                    # if [i + 1, j] is within bounds, then it becomes
                    # the next head. Otherwise, the element directly below
                    # i.e. the element [i, j + 1] becomes the next head
                    if row == N - 1:
                        col += 1
                    if row < N - 1:
                        row += 1
                # Flip the direction
                direction = 1 - direction
            else:
                row = new_row
                col = new_col
        return result
