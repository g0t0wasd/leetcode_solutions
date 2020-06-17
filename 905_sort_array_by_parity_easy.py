def sortArrayByParity(A):
    """
    Desription:
        Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
        You may return any answer array that satisfies this condition.
    Idea:
        Use two pointers
    Complexity:
        Time: O(n)
        Space: O(1)
    """
    i = 0
    for j in range(len(A)):
        if A[j] % 2 == 0:
            A[i], A[j] = A[j], A[i]
            i += 1
    return A
