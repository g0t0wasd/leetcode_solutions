def thirdMax(nums):
    """
    Description:
        Given a non-empty array of integers, return the third maximum number in this array.
        If it does not exist, return the maximum number. The time complexity must be in O(n).
    Idea:
        Since there will be only three numbers to care about - we can use three pointers
    Complexity:
        Time: O(n)
        Space: O(1)
    """
    top = mid = bot = float("-inf") # Use None if required
    for num in nums:
        if num in (top, mid, bot):
            continue
        if num > top:
            top, mid, bot = num, top, mid
        elif num > mid:
            mid, bot = num, mid
        elif num > bot:
            bot = num
    return top if bot == float("-inf") else bot
