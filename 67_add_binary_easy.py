class Solution:
    """
        Given two binary strings, return their sum (also a binary string).
        The input strings are both non-empty and contains only characters 1 or 0.

        Example 1:
        Input: a = "11", b = "1"
        Output: "100"

        Example 2:
        Input: a = "1010", b = "1011"
        Output: "10101"
    Idea:
        A. Convert strings to lists and pop the last element, add its value to carry,
            add modulo of carry to result and recalculate the remainder of the carry
        B. Use Python built-in function to convert from binary and back
        C. Calculate the legth of strings a and b, keep track of the carry based on the sum of
            that elements
    Complexity:
        A.
            Time: O(max(a, b))
            Space: O(a+b)
        B.
            Time: ?
            Space: ?
        C:
            Time: O(max(a,b))
            Space: O(1)
    """
    def addBinary(self, a: str, b: str) -> str:
#         carry = 0
#         a = list(a)
#         b = list(b)
#         res = ''
#         while a or b or carry:
#             if a:
#                 carry  += int(a.pop())
#             if b:
#                 carry += int(b.pop())
#             value = carry % 2
#             carry = carry // 2
#             res = str(value) + res
#         return res
        # B
        # return f"{int(a, 2) + int(b, 2):b}"
        # C
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        res = ""
        while i >= 0 or j >= 0 or carry != 0:
            if i >= 0:
                carry += 0 if a[i] == '0' else 1
                i -= 1
            if j >= 0:
                carry += 0 if b[j] == '0' else 1
                j -= 1
            res = str(carry % 2) + res
            carry = carry // 2
        return res
