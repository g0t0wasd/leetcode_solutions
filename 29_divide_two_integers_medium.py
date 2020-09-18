class Solution:
    """
    Description:
        Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

        Return the quotient after dividing dividend by divisor.

        The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

        Example 1:

        Input: dividend = 10, divisor = 3
        Output: 3
        Explanation: 10/3 = truncate(3.33333..) = 3.
        Example 2:

        Input: dividend = 7, divisor = -3
        Output: -2
        Explanation: 7/-3 = truncate(-2.33333..) = -2.
        Note:

        Both dividend and divisor will be 32-bit signed integers.
        The divisor will never be 0.
        Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
    Idea:
        Substract the divisor from the dividend while dividend is higher. Take care of negative numbers
        use quotient to speedup the process
    Complexity:
        Time: O(log n)
        Space: O(1)
    """
    def divide(self, dividend: int, divisor: int) -> int:
        negative = ((dividend < 0) != (divisor < 0))

        res = 0
        quotient = 1

        dividend = left = abs(dividend)
        divisor = right = abs(divisor)
        while left >= right:

            left -= right
            res += quotient
            quotient += quotient
            right += right

            if right > left:
                right = divisor
                quotient = 1

        if negative:
            return max(-res, -2147483648)
        return min(res, 2147483647)
