# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Description:
        Given a binary tree, return the inorder traversal of its nodes' values.
        Example:
        Input: [1,null,2,3]
           1
            \
             2
            /
           3

        Output: [1,3,2]
    Idea:
        Use recursion or stack. In case of stack traverse to the left node while node without left is found
        Then pick the latest item from stack and change to the right
    Complexity:
        Time: O(n)
        Space: O(n)
    """
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

        res = []
        stack = []

        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmp = stack.pop()
                res.append(tmp.val)
                root = tmp.right
        return res
