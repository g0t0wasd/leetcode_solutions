def reverseString(s):
    """
    Description:
        Write a function that reverses a string. The input string is given as an array of characters char[].
        Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
        You may assume all the characters consist of printable ascii characters.
    Idea:
        Use two pointers
    Complexity:
        Time: O(n)
        Space: O(1)
    """
    start = 0
    end = len(s) - 1
    while end > start:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1

    # Pythonic solution
    # s.reverse()
