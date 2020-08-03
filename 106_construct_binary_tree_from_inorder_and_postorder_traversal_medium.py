# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Description:
        Given inorder and postorder traversal of a tree, construct the binary tree.

        Note:
        You may assume that duplicates do not exist in the tree.

        For example, given

        inorder = [9,3,15,20,7]
        postorder = [9,15,7,20,3]
        Return the following binary tree:

            3
           / \
          9  20
            /  \
           15   7
    Idea:
        The last item in postorder is always the main root node. Find the node in
        inorder to split the tree into right and left branches. Use mapping to
        speed up the process of finding the root node in inorder.
    Complexity:
        Time: O(n)
        Space: O(n)
    """
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        tree_length = len(inorder)

        if tree_length == 0:
            return None
        self.mapping = {val: i for i, val in enumerate(inorder)}
        self.inorder = inorder
        self.postorder = postorder

        return self.rec(0, tree_length, 0, tree_length)

    def rec(self, istart, iend, pstart, pend):
        if istart >= iend or pstart >= pend:
            return None

        root = TreeNode(self.postorder[pend-1])
        root_index = self.inorder.index(self.postorder[pend-1])
        diff = root_index - istart
        root.left = self.rec(istart, istart + diff, pstart, pstart + diff)
        root.right = self.rec(istart + diff + 1, iend, pstart + diff, pend-1)
        return root
