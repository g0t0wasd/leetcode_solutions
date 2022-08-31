class Solution:

    MOD = 10 ** 9 + 7
    solutions = {}

    def rearrangeSticks(self, n, k):
        text_code = str(n) + "+" + str(k)
        if text_code in Solution.solutions:
            return Solution.solutions[text_code]
        # there is only one way to make all the sticks visible
        if n == k: return 1
        # no more sticks need to be shown
        if k == 0: return 0

        # case 1 - we pick the longest stick and make it visible. There is only one way to do this
        last_visible = self.rearrangeSticks(n - 1, k - 1)
        # case 2 - we pick hidden stick. There are n - 1 ways to do this
        last_hidden = self.rearrangeSticks(n - 1, k) * (n - 1)
        ans = (last_visible + last_hidden) % Solution.MOD
        Solution.solutions[text_code] = ans
        return ans


assert Solution().rearrangeSticks(5, 5) == 1
assert Solution().rearrangeSticks(3, 2) == 3
assert Solution().rearrangeSticks(20, 11) == 647427950
