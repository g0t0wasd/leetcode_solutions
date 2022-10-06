from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == k:
                res += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                left += 1

        return res


print(Solution().maxOperations([1, 2, 3, 4], 5))
print(Solution().maxOperations([3, 1, 3, 4, 3], 6))
print(Solution().maxOperations([3, 3, 3], 6))
print(Solution().maxOperations([2, 2, 2, 3, 1, 1, 4, 1], 4))
