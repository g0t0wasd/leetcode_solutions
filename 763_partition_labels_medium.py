class Solution:
    """
    Description:
        A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
        Example 1:

        Input: S = "ababcbacadefegdehijhklij"
        Output: [9,7,8]
        Explanation:
        The partition is "ababcbaca", "defegde", "hijhklij".
        This is a partition so that each letter appears in at most one part.
        A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
    Idea:
        Store the last occurence of every letter. Update the right pointer to match the last entry of current letter.
        If the index of current letter and rightmost match - it's the end of the split
    Complexity:
        Time: O(n)
        Space: O(1)
    """
    def partitionLabels(self, S: str) -> List[int]:
        table = {ch: i for i, ch in enumerate(S)}
        left = 0
        right = 0
        res = []

        for i, ch in enumerate(S):
            right = max(right, table[ch])
            if right == i:
                res.append(right - left + 1)
                left = i + 1
        return res
