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

    # Top Bottom appoach
    # We pass the increasing depth through the recursion
    answer = 0

    def maxDepth(self, root: TreeNode) -> int:
        self.top_bottom(root, 1)
        return self.answer

    def top_bottom(self, root, depth):
        if not root:
            return 0

        if not root.left and not root.right:
            self.answer = max(self.answer, depth)

        self.top_bottom(root.left, depth+1)
        self.top_bottom(root.right, depth+1)
