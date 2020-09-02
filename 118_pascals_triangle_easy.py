class Solution:
    """
    Description:
        Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
                    1
                   1 1
                  1 2 1
                 1 3 3 1
                1 4 6 4 1
        In Pascal's triangle, each number is the sum of the two numbers directly above it.
    Idea:
        Use DP to access values of previous row
    Complexity:
        Time: O(n**2)
        Space: O(n**2)
    """
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        res = [[1]]

        for i in range(1, numRows):
            prev_array = res[i-1]
            cur_array = [1]
            for j in range(1, i):
                val = prev_array[j-1] + prev_array[j]
                cur_array.append(val)
            cur_array.append(1)
            res.append(cur_array)
        return res
