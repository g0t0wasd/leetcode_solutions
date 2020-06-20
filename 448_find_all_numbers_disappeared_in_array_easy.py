def findDisappearedNumbers(nums):
    """
    Description:
        Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
        Find all the elements of [1, n] inclusive that do not appear in this array.
        Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
    Idea:
        On the iteration we need to mark every present item somehow. Since we know from definition that all entries are > 1
        we can set them as negative. And later on next loop just filter all the positive items
    Complexity:
        Time: O(n)
        Space: O(1). Returning array doesn't count as additional space
    """
    res = []
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        if nums[index] > 0:
            nums[index] = -nums[index]
    for i in range(len(nums)):
        if nums[i] > 0:
            res.append(i+1)
    return res
