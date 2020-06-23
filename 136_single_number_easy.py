def singleNumber(nums):
    """
    Description:
        Given a non-empty array of integers, every element appears twice except for one. Find that single one.
        Note:
        Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
    Idea:
        A: use hashtable to count occurences
        B: use XOR bit operation. XOR will return 1 only on two different bits. So if two numbers are the same, XOR will return 0. Finally only one number left.
    Complexity:
        A:
            Time: O(n)
            Space: O(n)
        B:
            Time: O(n)
            Space: O(1)
    """

    # A
    times_seen = {}
    for item in nums:
        if item in times_seen:
            times_seen[item] += 1
        else:
            times_seen[item] = 1
    for key, value in times_seen.items():
        if value == 1:
            return key

    # B
    a = 0
    for item in nums:
        a ^= item
    return a
