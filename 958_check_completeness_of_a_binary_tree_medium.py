# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Description:
        Given a binary tree, determine if it is a complete binary tree.
        Definition of a complete binary tree from Wikipedia:
        In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
    Idea:
        Traverse a tree from top to bottom with a flag which identifies if we have a missing node
    Complexity:
        Time: O(n)
        Space: O(n)
    """
    def isCompleteTree(self, root: TreeNode) -> bool:
        have_null = False

        queue = [root]

        while queue:
            node = queue.pop(0)
            if not node:
                have_null = True
                continue

            if have_null:
                return False
            queue.append(node.left)
            queue.append(node.right)
        return True
