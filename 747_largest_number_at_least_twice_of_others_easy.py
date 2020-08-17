class Solution:
    """
    Description:
        In a given integer array nums, there is always exactly one largest element.
        Find whether the largest element in the array is at least twice as much as every other number in the array.
        If it is, return the index of the largest element, otherwise return -1.
    Idea:
        Iterate recording max and second max, so we iterate only once
    Complexity:
        Time: O(n)
        Space: O(1)
    """
    def dominantIndex(self, nums: List[int]) -> int:
        largest = 0
        second = 0
        index = 0

        for i, num in enumerate(nums):
            if num > largest:
                second = largest
                largest = num
                index = i
            elif num > second:
                second = num
        if second * 2 <= largest:
            return index

        return -1
