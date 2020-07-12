# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        Description:
            Given a linked list, remove the n-th node from the end of list and return its head.
            Example:
            Given linked list: 1->2->3->4->5, and n = 2.
            After removing the second node from the end, the linked list becomes 1->2->3->5.
            Note:
            Given n will always be valid.
            Follow up:
            Could you do this in one pass?
        Idea: Use two pointers and move slow only after fast is pass n items from slow
        Complexity:
            Time: O(n)
            Space: O(1)
        """
        slow = fast = head
        length = 1
        while fast.next:
            length += 1
            fast = fast.next
            if length > n + 1:
                slow = slow.next

        if length == n:
            return head.next
        else:
            slow.next = slow.next.next
            return head
