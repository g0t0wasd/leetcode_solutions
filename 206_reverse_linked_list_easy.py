# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Description:
        Reverse a singly linked list.
        Example:
        Input: 1->2->3->4->5->NULL
        Output: 5->4->3->2->1->NULL
        Follow up:
        A linked list can be reversed either iteratively or recursively. Could you implement both?
    Idea:
        Keep track of a head and pop the nodes, create holder for main list
    Complexity:
        Time: O(n)
        Space: O(1)
    """
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return
        cur_head = head
        while head.next:
            tmp = head.next
            head.next = tmp.next
            tmp.next = cur_head
            cur_head = tmp
        return cur_head
