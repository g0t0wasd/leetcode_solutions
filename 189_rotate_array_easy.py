def rotate(nums, k):
    """
    Description:
        Given an array, rotate the array to the right by k steps, where k is non-negative.
        Follow up:
            Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
            Could you do it in-place with O(1) extra space?
    Idea:
        A: brute forse approach
        B: python slicing
        C: rotation without python slicing
    Complexity:
        A:
            Time: O(n)
            Space: O(1)
        B:
            Time: O(n)
            Space: O(n) looks like python slicing takes additional space
        C:
            Time: O(n)
            Space: O(1)
    """

    # A

    # i = 0
    # while i < k:
    #     nums.insert(0, nums.pop(-1))
    #     i += 1

    # B

    # k = k % len(nums)
    # if k == 0: return
    # nums[:k], nums[k:] = nums[-k:], nums[:-k]

    # C

    k = k % len(nums)
    turn(nums, 0, len(nums) - 1)
    turn(nums, 0, k - 1)
    turn(nums, k, len(nums) - 1)


def turn(nums, start, end):
    while start < end:
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start += 1
        end -= 1
