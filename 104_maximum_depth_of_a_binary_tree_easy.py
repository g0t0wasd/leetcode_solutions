# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Description:
        Given a binary tree, find its maximum depth.
        The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

        Note: A leaf is a node with no children.

        Example:

        Given binary tree [3,9,20,null,null,15,7],

            3
           / \
          9  20
            /  \
           15   7
        return its depth = 3.
    Idea:
        Use recursion and on each level add one
    Complexity:
        Time: O(n)
        Space: O(n)
    """

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
