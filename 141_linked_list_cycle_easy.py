# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        Description:
            Given a linked list, determine if it has a cycle in it.
            To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
        Idea:
            Use two pointers
        Complexity:
            Time: O(n)
            Space: O(1)
        """

        slow_pointer = head
        fast_pointer = head

        while fast_pointer is not None and fast_pointer.next is not None:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

            if fast_pointer == slow_pointer:
                return True
        return False
