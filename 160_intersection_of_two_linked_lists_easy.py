# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    """
    Description:
        Write a program to find the node at which the intersection of two singly linked lists begins.
        Notes:
        If the two linked lists have no intersection at all, return null.
        The linked lists must retain their original structure after the function returns.
        You may assume there are no cycles anywhere in the entire linked structure.
        Each value on each linked list is in the range [1, 10^9].
        Your code should preferably run in O(n) time and use only O(1) memory.
    Idea:
        Use two pointers. In order to match the size - reassign pointer to counterpart head. (possible to compare length)
    Complexity:
        Time: O(n)
        Space: O(1)
    """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        q, p = headA, headB

        while q != p:
            q = q.next if q else headB
            p = p.next if p else headA

        return q
