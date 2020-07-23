# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Description:
        Given a linked list, rotate the list to the right by k places, where k is non-negative.
        Example 1:

        Input: 1->2->3->4->5->NULL, k = 2
        Output: 4->5->1->2->3->NULL
        Explanation:
        rotate 1 steps to the right: 5->1->2->3->4->NULL
        rotate 2 steps to the right: 4->5->1->2->3->NULL
    Idea:
        Calculate length and use two pointers, don't forget that k may be very big.
        It is also possible to form a circle: make tail point to the head and then - rotate it
    Complexity:
        Time: O(n)
        Space: O(1)
    """
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head

        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1

        rotate_times = k % length

        if rotate_times == 0:
            return head

        slow_p = fast_p = head
        for _ in range(rotate_times):
            fast_p = fast_p.next

        while fast_p.next:
            fast_p = fast_p.next
            slow_p = slow_p.next

        tmp = slow_p.next
        slow_p.next = None
        fast_p.next = head
        return tmp
