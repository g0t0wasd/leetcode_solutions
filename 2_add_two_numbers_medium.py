class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_number(l1, l2):
    """
    Description:
        You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
        You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    Idea:
        Use modulus division to get correct result and carried.
    Complexity:
        Time: O(n)
        Space: O(n)
    """
    carried = 0
    answer = current = ListNode() 
    while l1 or l2 or carried:
        if l1:
            carried += l1.val
            l1 = l1.next
        if l2:
            carried += l2.val
            l2 = l2.next
        carried, res = divmod(carried, 10)
        current.next = current = ListNode(res)
    return answer.next
