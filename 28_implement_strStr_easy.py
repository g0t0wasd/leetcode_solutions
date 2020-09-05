class Solution:
    """
    Description:
        Implement strStr().
        Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

        Example 1:
        Input: haystack = "hello", needle = "ll"
        Output: 2

        Example 2:
        Input: haystack = "aaaaa", needle = "bba"
        Output: -1

        Clarification:
        What should we return when needle is an empty string? This is a great question to ask during an interview.
    Idea:
        A. Brute force approach
        B. KMP (Knuth-Morris-Pratt) approach - generate lookup array which will show how far deep we need to go back
    Complexity:
        A:
            Time: O(m*n) (text length * substring length)
            Space: O(1)
        B:
            Time: O(m + n)
            Space: O(n)
    """
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
#         haystack_len = len(haystack) # 5
#         needle_len = len(needle) # 2
#         i = 0
#         while i <= haystack_len - needle_len: # 3
#             if haystack[i] == needle[0]:
#                 if haystack[i:i+needle_len] == needle:
#                     return i
#             i += 1
#         return -1

        lps = self.generateLPS(needle)
        haystack_index = 0
        needle_index = 0
        while haystack_index < len(haystack):
            if haystack[haystack_index] == needle[needle_index]:
                haystack_index += 1
                needle_index += 1
            else:
                if needle_index > 0:
                    needle_index = lps[needle_index - 1]
                else:
                    haystack_index += 1
                    needle_index = 0
            if needle_index == len(needle):
                return haystack_index - needle_index

        return -1

    def generateLPS(self, substr):
        """ Longest prefix which is also a suffix """
        sub_len = len(substr)
        lps = [0] * sub_len

        index = 0
        i = 1
        while i < sub_len:
            if substr[i] == substr[index]:
                index += 1
                lps[i] = index
                i += 1
            else:
                if index > 0:
                    index = lps[index - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
