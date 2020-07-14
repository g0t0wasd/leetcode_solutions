# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Description:
        Remove all elements from a linked list of integers that have value val.
        Example:
        Input:  1->2->6->3->4->5->6, val = 6
        Output: 1->2->3->4->5
    Idea:
        Iterate over items while reassigning the next nodes.
    Complexity:
        Time: O(n)
        Space: O(1)
    """
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        parent = ListNode(42, head)
        head = parent
        while head and head.next:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return parent.next
