from typing import List


class Solution:
    """
    You are given a string num, which represents a large integer. You are also given a 0-indexed integer array change of length 10 that maps each digit 0-9 to another digit. More formally, digit d maps to digit change[d].

    You may choose to mutate a single substring of num. To mutate a substring, replace each digit num[i] with the digit it maps to in change (i.e. replace num[i] with change[num[i]]).

    Return a string representing the largest possible integer after mutating (or choosing not to) a single substring of num.

    A substring is a contiguous sequence of characters within the string.
    """

    def maximumNumber(self, num: str, change: List[int]) -> str:
        num = list(num)
        mutate = False

        for i, ch in enumerate(num):
            x = int(ch)
            if change[x] > x:
                mutate = True
                num[i] = str(change[x])
            elif x > change[x] and mutate:
                break
        return "".join(num)


assert(Solution().maximumNumber("132", [9, 8, 5, 0, 3, 6, 4, 2, 6, 8]) == "832")
assert(Solution().maximumNumber("021", [9, 4, 3, 5, 7, 2, 1, 9, 0, 6]) == "934")
assert(Solution().maximumNumber("5", [1, 4, 7, 5, 3, 2, 5, 6, 9, 4]) == "5")
assert(Solution().maximumNumber("330", [9, 3, 6, 3, 7, 3, 1, 4, 5, 8]) == "339")
assert(Solution().maximumNumber("334111", [0, 9, 2, 3, 3, 2, 5, 5, 5, 5]) == "334999")
