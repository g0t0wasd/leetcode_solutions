def duplicate(arr):
    """
    Description:
        Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
        Note that elements beyond the length of the original array are not written.
        Do the above modifications to the input array in place, do not return anything from your function.
    Idea:
        To ease the array shifting it's better to start from the end and take into account number of zeroes - see how far we should shift each particular element
    Complexity:
        Time: O(n)
        Space: O(1)
    """
    zeroes = arr.count(0)
    arr_len = len(arr)
    for i in range(arr_len - 1, -1, -1):
        if i + zeroes < arr_len:
            arr[i + zeroes] = arr[i]
        if arr[i] == 0:
            zeroes -= 1
            if i + zeroes < arr_len:
                arr[i + zeroes] = 0
