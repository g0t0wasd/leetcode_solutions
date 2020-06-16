def moveZeroes(nums):
    """
    Description:
        Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
    Idea:
        Use two pointer to check the array
    Complexity:
        Time: O(n) - iterate over all the array
        Space: O(n) - in-place operation
    """
    slow_index = 0
    for fast_index in range(len(nums)):
        if nums[fast_index] != 0:
            nums[slow_index], nums[fast_index] = nums[fast_index], nums[slow_index]
            slow_index += 1
