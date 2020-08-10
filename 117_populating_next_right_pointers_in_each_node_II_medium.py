# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None,
                 next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    """
    Description:
        Given a binary tree

        struct Node {
          int val;
          Node *left;
          Node *right;
          Node *next;
        }
        Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
        Initially, all next pointers are set to NULL.
        Follow up:
        You may only use constant extra space.
        Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
    Idea:
        Iterate over nodes with a nested loop while keeping pointers to point to leftmost dummy node and a head
    Complexity:
        Space: O(1)
        Time: O(n)
    """
    def connect(self, root: 'Node') -> 'Node':
        # if not root:
        #     return root
        # stack = [[root]]
        # result = []
        # while stack:
        #     cur_level = stack.pop()
        #     next_level = []
        #     for node in cur_level:
        #         if node.left:
        #             next_level.append(node.left)
        #         if node.right:
        #             next_level.append(node.right)
        #     result.append(next_level)
        #     if next_level:
        #         stack.append(next_level)
        # for entry in result:
        #     for i in range(len(entry) - 1):
        #         if entry[i]:
        #             entry[i].next = entry[i+1]
        # return root

        cur = root
        dummy = Node()
        kid = dummy

        while cur:  # passing in depth
            while cur:  # passing in width
                if cur.left:
                    kid.next = cur.left
                    kid = kid.next
                if cur.right:
                    kid.next = cur.right
                    kid = kid.next
                cur = cur.next
            cur = dummy.next
            kid.next = None
            kid = dummy

        return root
