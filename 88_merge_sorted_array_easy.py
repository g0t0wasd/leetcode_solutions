def merge(nums1, m, nums2, n):
    """
    Description:
        Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
        Note:
            The number of elements initialized in nums1 and nums2 are m and n respectively.
            You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
    Idea:
        Iterate from the end of smallest array and position of the biggest array.
        Perform merging based on the comparison
    Complexity:
        Time: O(n)
        Space: O(1)
    """
    last_nums1 = m - 1
    last_nums2 = n - 1
    index = len(nums1) - 1
    while last_nums2 >= 0:
        if last_nums1 < 0:
            num1_number = - 10000000000
        else:
            num1_number = nums1[last_nums1]
        num2_number = nums2[last_nums2]
        if num1_number >= num2_number:
            nums1[index] = num1_number
            last_nums1 -= 1
        else:
            nums1[index] = num2_number
            last_nums2 -= 1
        index -= 1
