class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Description:
         You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

        You may assume the two numbers do not contain any leading zero, except the number 0 itself.

        Follow up:
        What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

        Example:

        Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
        Output: 7 -> 8 -> 0 -> 7
    Idea:
        Use stack to store the numbers and then just calculate backwards
    Complexity:
        Time: O(n) We iterate each linked list twice
        Space: O(n) We use stacks
    """
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = []
        s2 = []

        while l1:
            s1.append(l1.val)
            l1 = l1.next

        while l2:
            s2.append(l2.val)
            l2 = l2.next

        carry = 0
        res = None
        while s1 or s2 or carry:
            if s1:
                carry += s1.pop()
            if s2:
                carry += s2.pop()

            new_node = ListNode(carry % 10)
            new_node.next = res
            res = new_node

            carry //= 10

        return res
