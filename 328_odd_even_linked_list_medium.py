# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Description:
        Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
        You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

        Example 1:

        Input: 1->2->3->4->5->NULL
        Output: 1->3->5->2->4->NULL

        Example 2:
        Input: 2->1->3->5->6->4->7->NULL
        Output: 2->3->6->7->1->5->4->NULL
    Idea:
        Create two heads to hold odd / even.
    Complexity:
        Time: O(n)
        Space: O(1) - we always have only four more pointers
    """
    def oddEvenList(self, head: ListNode) -> ListNode:
        head_odd = odd_cur = ListNode("odd")
        head_even = even_cur = ListNode("even")
        while head:
            odd_cur.next = head
            even_cur.next = head.next
            odd_cur = odd_cur.next
            even_cur = even_cur.next
            head = head.next.next if even_cur else None
        odd_cur.next = head_even.next
        return head_odd.next
