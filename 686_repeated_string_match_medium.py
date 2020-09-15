class Solution:
    """
    Description:
        Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. If it is impossible for b​​​​​​ to be a substring of a after repeating it, return -1.
        Notice: string "abc" repeated 0 times is "",  repeated 1 time is "abc" and repeated 2 times is "abcabc".

        Example 1:

        Input: a = "abcd", b = "cdabcdab"
        Output: 3
        Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.
        Example 2:

        Input: a = "a", b = "aa"
        Output: 2
        Example 3:

        Input: a = "a", b = "a"
        Output: 1
        Example 4:

        Input: a = "abc", b = "wxyz"
        Output: -1
    Idea:
        Calculate the smallest possible number of repetitions of a, it could be either length of b / a or b / a + 1
    Complexity:
        Time: O(N * (N + M))
        Space: O(M + N)
    """
    def repeatedStringMatch(self, a: str, b: str) -> int:
        times = -(-len(b) // len(a))  # ceiling operation, floor rounds to the lowest integer

        for i in range(2):
            if b in (a * (times + i)):
                return times + i
        return -1
