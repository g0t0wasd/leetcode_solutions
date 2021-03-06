# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Description:
        Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.
        Example:

        Input: 1->2->4, 1->3->4
        Output: 1->1->2->3->4->4
    Idea:
        Merging part of a merge sort
    Complexity:
        Time: O(n)
        Space: O(1)
    """
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode('head')
        cur = head
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return head.next
