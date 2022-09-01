from typing import List


class Solution:
    """
    You are given an n x n integer matrix. You can do the following operation any number of times:
        - Choose any two adjacent elements of matrix and multiply each of them by -1.
    Two elements are considered adjacent if and only if they share a border.
    Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

    Idea: basically, we care only if the number of negative values is odd or even.
        If it's odd we repeat the algorithm until the only negative entry is the lowest (so we have to deduce it two times)
        If it's even: just flip the signs until all numbers are positive
    """

    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        min_value = float('inf')
        total_min = 0

        for row in matrix:
            for cell in row:
                av = abs(cell)
                if av < min_value:
                    min_value = av

                total_sum += av

                if cell < 0:
                    total_min += 1

        if total_min % 2 == 0:
            return total_sum
        return total_sum - min_value * 2


assert Solution().maxMatrixSum([[1,-1], [-1,1]]) == 4
assert Solution().maxMatrixSum([[1,2,3], [-1,-2,-3], [1,2,3]]) == 16
