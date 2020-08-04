# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    """
    Description:
        You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
        struct Node {
          int val;
          Node *left;
          Node *right;
          Node *next;
        }
        Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

        Initially, all next pointers are set to NULL.
    Idea:
        1. Iterate over left leaves with correct pointing. Notice that initially all .next points to None
        2. Generate all the levels of the tree and bind one to another
    Complexity:
        Time: O(n)
        Space: O(1)
    """
    def connect(self, root: 'Node') -> 'Node':
        # if not root:
        #     return root
        # stack = [[root]]
        # answer = []
        # while stack:
        #     cur_level = stack.pop()
        #     answer.append(cur_level)
        #     next_level = []
        #     for node in cur_level:
        #         if node.left:
        #             next_level.append(node.left)
        #             next_level.append(node.right)
        #     if next_level:
        #         stack.append(next_level)
        # for level in answer:
        #     for i in range(len(level) - 1):
        #         level[i].next = level[i + 1]
        #     level[-1].next = None
        # return root

        if not root:
            return root

        cur = root
        next_node = root.left

        while cur.left:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
                cur = cur.next
            else:
                cur = next_node
                next_node = next_node.left
        return root

        # cur = root
        # while cur and cur.left:
        #     next = cur.left
        #     while cur:
        #         cur.left.next = cur.right
        #         cur.right.next = cur.next and cur.next.left
        #         cur = cur.next
        #     cur = next
        # return root
