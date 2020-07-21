# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    """
    Description:
        A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
        Return a deep copy of the list.
        The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
        val: an integer representing Node.val
        random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
    Idea:
        Main problem is absence of *new* random node to point to.
        So use either HashTable or point cur.next to new node to another and few passes throught the nodes
    Complexity:
        Time: O(n)
        Space: O(n) with hashtable and O(1) without

    """
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
         table = {}
         cur = head
         while cur:
             table[cur] = Node(cur.val)
             cur = cur.next

         cur = head
         while cur:
             table[cur].next = table[cur.next] if cur.next else None
             table[cur].random = table[cur.random] if cur.random else None
             cur = cur.next
         return table[head] if head else None
     """

        if not head:
            return head
        cur = head
        while cur:
            new_node = Node(cur.val)
            new_node.next = cur.next
            cur.next = new_node
            cur = cur.next.next

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        new_head = head.next
        pold = head
        pnew = new_head
        while pnew.next:
            pold.next = pnew.next
            pold = pold.next
            pnew.next = pold.next
            pnew = pnew.next

        pnew = None
        pold = None
        return new_head
