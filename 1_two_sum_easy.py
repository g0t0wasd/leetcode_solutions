def two_sum(nums, target):
    """
    Description:
        Given an array of integers, return indices of the two numbers such that they add up to a specific target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Idea:
        Iterate over the elements and fill the HashMap with the difference(target - current_item) as the key and index as value.
        So when we hit the complement we will instantly know the index.
    Complexity:
        Time complexity: O(n). Iterate over list only once and get the element from HashTable with O(1).
        Space complexity: O(n). Extra space for the HashTable.
    """
    values = {}
    for i, item in enumerate(nums):
        if item in values:
            return [values[item], i]
        else:
            values[target - item] = i
