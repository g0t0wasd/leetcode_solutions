class Solution:

    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     self.memo = {}
    #     return self.finder(text1, text2, 0, 0)

    # def finder(self, text1, text2, i, j):
    #     if (i, j) in self.memo:
    #         return self.memo[(i, j)]

    #     if i == len(text1) or j == len(text2):
    #         return 0

    #     if text1[i] == text2[j]:
    #         res = 1 + self.finder(text1, text2, i + 1, j + 1)
    #         self.memo[(i, j)] = res
    #         return res
    #     else:
    #         a = self.finder(text1, text2, i + 1, j)
    #         self.memo[(i + 1, j)] = a
    #         b = self.finder(text1, text2, i, j + 1)
    #         self.memo[(i, j + 1)] = b
    #         return max(a, b)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # DP solution
        dp = [[0] * len(text1) for _ in text2]

        for i, char in enumerate(text2):
            for j, char2 in enumerate(text1):
                if char == char2:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]


print(Solution().longestCommonSubsequence("abcde", "ace"))
print(Solution().longestCommonSubsequence("ace", "abcde"))
print(Solution().longestCommonSubsequence("abc", "abc"))
print(Solution().longestCommonSubsequence("abc", "def"))
print(Solution().longestCommonSubsequence("acotan", "cata"))
