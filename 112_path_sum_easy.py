# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Description:
        Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
        Note: A leaf is a node with no children.
        Example:

        Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
        return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
    Idea:
        Accumulate the sum while traversing the tree. It's possible to use stack, queue
        and addition / substraction for accumulation of result
    Complexity:
        Time: O(n)
        Space: O(n)
    """
    def hasPathSum(self, root: TreeNode, count: int) -> bool:
        if not root:
            return False
        queue = [(root, root.val)]
        while queue:
            node, node_val = queue.pop(0)
            if not node.left and not node.right:
                if node_val == count:
                    return True
            if node.left:
                queue.append((node.left, node_val + node.left.val))
            if node.right:
                queue.append((node.right, node_val + node.right.val))
        return False

    def hasPathSum(self, root, count):
        if not root:
            return False

        if not root.left and not root.right and root.val == count:
            return True

        count -= root.val

        return self.hasPathSum(root.left, count) or self.hasPathSum(root.right, count)
