def validMountainArray(A):
    """
    Description:
        Given an array A of integers, return true if and only if it is a valid mountain array.
        Recall that A is a mountain array if and only if:
            A.length >= 3
            There exists some i with 0 < i < A.length - 1 such that:
                A[0] < A[1] < ... A[i-1] < A[i]
                A[i] > A[i+1] > ... > A[A.length - 1]
    Idea:
        Walk uphill and downhill
    Complexity:
        Time: O(n)
        Space: O(1)
    """
    if len(A) < 3 or A[0] > A[1]:
        return False
    uphill = True
    i = 1
    while i < len(A):
        if uphill:
            if A[i] <= A[i-1]:
                uphill = False
        if not uphill:
            if A[i] >= A[i-1]:
                return False
        i += 1
    return not uphill
