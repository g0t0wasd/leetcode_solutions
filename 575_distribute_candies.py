from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        half = len(candyType) // 2
        unique = len(set(candyType))
        return unique if unique < half else half


print(Solution().distributeCandies([1,1,2,2,3,3]))
print(Solution().distributeCandies([1,1,2,3]))
print(Solution().distributeCandies([6,6,6,6]))
