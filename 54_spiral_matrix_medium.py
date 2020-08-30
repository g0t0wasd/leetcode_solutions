class Solution:
    """
        Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
        Example 1:
        Input:
        [
         [ 1, 2, 3 ],
         [ 4, 5, 6 ],
         [ 7, 8, 9 ]
        ]
        Output: [1,2,3,6,9,8,7,4,5]
        Example 2:

        Input:
        [
          [1, 2, 3, 4],
          [5, 6, 7, 8],
          [9,10,11,12]
        ]
        Output: [1,2,3,4,8,12,11,10,9,5,6,7]
    Idea:
        A. Iterate the over all the indexes using the direction and index pointers
        B. Use Python matrix transposition
    Complexity:
        A:
            Time: O(N), where N is number of elements
            Space: O(1)
        B:
            Time: Depends on sizes??
            Space: O(N)
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         res = []
#         if len(matrix) == 0 or len(matrix[0]) == 0:
#             return res
#         row_start = 0
#         col_start = 0
#         row_end = len(matrix) - 1
#         col_end = len(matrix[0]) - 1
#         while (col_start <= col_end and row_start <= row_end):
#             for i in range(col_start, col_end + 1):
#                 res.append(matrix[row_start][i])
#             row_start += 1
#             for i in range(row_start, row_end + 1):
#                 res.append(matrix[i][col_end])
#             col_end -= 1
#             if (row_start <= row_end):
#                 for i in range(col_end, col_start - 1, -1):
#                     res.append(matrix[row_end][i])
#                 row_end -= 1
#             if (col_start <= col_end):
#                 for i in range(row_end, row_start - 1, -1):
#                     res.append(matrix[i][col_start])
#                 col_start += 1

        res = []
        while matrix:
            res.extend(matrix.pop(0))
            matrix = [*zip(*matrix)][::-1]
        return res
