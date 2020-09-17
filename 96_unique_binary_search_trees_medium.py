class Solution:
    """
    Description:
        Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

        Example:

        Input: 3
        Output: 5
        Explanation:
        Given n = 3, there are a total of 5 unique BST's:

           1         3     3      2      1
            \       /     /      / \      \
             3     2     1      1   3      2
            /     /       \                 \
           2     1         2                 3
    Idea:
        A:
            To calculate the number of BST of an n, we need to calculate number of BST of an n - 1 and so on.
            Since it's a BSearchT, every node i from 1 to n will have exactly i - 1 nodes to the left multiplied by n - i
            nodes to the right. We also use memoization to speed up the process
        B:
            We can solve this in classical dynamic programming way with O(n^2) complexity. However we can recognize in this formula Catalan Numbers: https://en.wikipedia.org/wiki/Catalan_number and there is direct formula to evaluate them:
            f[n] = (2n)!/(n! * n! * (n+1)).

class Solution:
    Complexity:
        A:
            Time: O(n ** 2)
            Space: O(n)
        B:
            Time: O(n**2) time complexity is O(n) to evaluate all factorials,
            Space: O(1)
    """
    cache = dict()

    def numTrees(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1

        if n in self.cache:
            return self.cache.get(n)

        count = 0
        for i in range(1, n + 1):
            count += self.numTrees(i-1) * self.numTrees(n-i)
        self.cache[n] = count
        return self.cache.get(n)

    # def numTrees(self, n):
        # return factorial(2*n)//factorial(n)//factorial(n)//(n+1)
