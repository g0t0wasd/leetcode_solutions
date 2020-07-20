class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    """
    Description:
        You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.
        Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.
    Idea:
        Use stack to keep track of the childrens. No idea why they need a doubly linked list
    Complexity:
        Time: O(n)
        Space: O(n)
    """
    def flatten(self, head):
        if not head:
            return

        dummy = Node(None, None, head, None)
        stack = [head]
        prev = dummy

        while stack:
            root = stack.pop()

            root.prev = prev
            prev.next = root

            if root.next:
                stack.append(root.next)
                root.next = None

            if root.child:
                stack.append(root.child)
                root.child = None

            prev = root

        dummy.next.prev = None
        return dummy.next
