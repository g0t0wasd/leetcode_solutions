# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Description:
        Given a binary tree, return the preorder traversal of its nodes' values.
        Example:
        Input: [1,null,2,3]
           1
            \
             2
            /
           3
        Output: [1,2,3]
    Idea:
       1. Use stack for iterative solution (right node should be added first)
       2. Use recursion with [] + rec()
    """
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # Iterative solution

        # res = []
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     if node:
        #         res.append(node.val)
        #         stack.append(node.right)
        #         stack.append(node.left)
        # return res

        # Recursive solution
        return [] if not root else [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
