def containsDuplicate(nums):
    """
    Description:
        Given an array of integers, find if the array contains any duplicates.
        Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
    Idea:
        Use hastTable or set to keep track of what we've already seen
    Complexity:
        Time: O(n)
        Space: O(n)
    """
    # seen = set()
    # for item in nums:
    #     if item in seen:
    #         return True
    #     seen.add(item)
    # return False
    return len(nums) > len(set(nums))
