# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Description:
        Given a singly linked list, determine if it is a palindrome.

        Example 1:
        Input: 1->2
        Output: false

        Example 2:
        Input: 1->2->2->1
        Output: true

        Follow up:
        Could you do it in O(n) time and O(1) space?
    Idea:
        rotate the half of the linked list and compare
    Complexity:
        Time: O(n)
        Space: O(1), O(n) for Python solution
    """
    def isPalindrome(self, head: ListNode) -> bool:
        # res = []
        # while head:
        #     res.append(head.val)
        #     head = head.next
        # return res == res[::-1]
        if not head or not head.next:
            return True

        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # At this point slow is pointing to the half of the LL

        # This is the rotation part
        prev = None
        while slow:
            slow.next, slow, prev = prev, slow.next, slow

        first = head
        second = prev

        while first and second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True
