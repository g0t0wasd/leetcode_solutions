def replaceElements(arr):
    """
    Description:
        Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
        After doing so, return the array.
    Idea:
        Iterate from the end, use either tuple assignment or additional variable, so no item is lost
    Complexity:
        Time: O(n) - iterate over all array
        Space: O(1) - inplace operation
    """
    max_el, arr[-1] = arr[-1], -1
    index = len(arr) - 2
    while index >= 0:
        arr[index], max_el = max_el, max(max_el, arr[index])
        index -= 1
    return arr
