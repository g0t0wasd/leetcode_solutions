from typing import List


class Comparator(str):
    def __lt__(self, other):
        return self + other > other + self


class Solution:
    def largestNumber(self, nums: List) -> str:
        res = "".join(sorted(map(str, nums), key=Comparator))
        return '0' if res[0] == '0' else res


print(Solution().largestNumber([10, 2]))
print(Solution().largestNumber([3, 30, 34, 5, 9]))
print(Solution().largestNumber([5, 52]))
print(Solution().largestNumber([5, 57]))
print(Solution().largestNumber([0, 0, 0]))
