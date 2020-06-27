def plusOne(digits):
    """
    Description:
        Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
        The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
        You may assume the integer does not contain any leading zero, except the number 0 itself.
    Idea:
        A: Python fun
        B: while loop
        C: for loop
    Complexity:
        A:
            Time: O(n) - complexity of join
            Space: O(n)
        B:
            Time: O(n)
            Space: O(1)
        C:
            Time: O(n)
            Space: O(1)
    """
    # Approach A
    # return list(str(int("".join(map(str, digits))) + 1))

    # Approach B
    # carry = True
    # index = len(digits) - 1
    # while carry:
    #     carry = False
    #     if digits[index] == 9:
    #         digits[index] = 0
    #         if index == 0:
    #             digits.insert(0, 1)
    #         else:
    #             carry = True
    #             index -= 1
    #     else:
    #         digits[index] += 1
    # return digits

    # Approach C
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + [0] * len(digits)
