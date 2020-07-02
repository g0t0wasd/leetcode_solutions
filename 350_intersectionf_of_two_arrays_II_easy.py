def intersect(nums1, nums2):
    """
    Description:
        Given two arrays, write a function to compute their intersection.
        Note:
            Each element in the result should appear as many times as it shows in both arrays.
            The result can be in any order.
        Follow up:
            What if the given array is already sorted? How would you optimize your algorithm?
            What if nums1's size is small compared to nums2's size? Which algorithm is better?
            What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
    Idea:
        Iterate over the elements and count the occurences.
        If the arrays are already sorted it is possible to use two pointers technique
    Complexity:
        Time: O(n)
        Space: O(n)
    """
    if len(nums1) < len(nums2):
        target, other = nums1, nums2
    else:
        target, other = nums2, nums1

    result = []
    for item in target:
        if item in other:
            result.append(item)
            other.remove(item)
    return result
