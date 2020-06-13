def checkIfExist(arr):
    """
    Description:
        Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).
    Idea:
        Add lookup container to which we will be adding half and double the current item
    Complexity:
        Time: O(n)
        Space: O(n)
    """
    content = set()
    for item in arr:
        if item in content:
            return True
        else:
            if item % 2 == 0:
                content.add(item / 2)
            content.add(item*2)
    return False
