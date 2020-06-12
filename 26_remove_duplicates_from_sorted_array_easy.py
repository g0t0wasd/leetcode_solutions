def removeDuplicates(nums):
    """
    Description:
        Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
        Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
    Idea:
        Use two pointers to swap items
    Complexity:
        Time: O(n). We need to iterate over all array
        Space: O(1). In place
    """
    length = len(nums)
    if length == 0:
        return 0
    i = 0
    for j in range(1, length):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1
