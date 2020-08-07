# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Description:
        Given preorder and inorder traversal of a tree, construct the binary tree.
        Note:
        You may assume that duplicates do not exist in the tree.

        For example, given

        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        Return the following binary tree:

            3
           / \
          9  20
            /  \
           15   7
    Idea:
        The first item in preoprder is always main root node. Find the node in
        inorder and split the list into left / right part. Use mapping to speedup
        the process. Use correct indexing to get correct splits

    Complexity:
        Time: O(n)
        Space: O(n)
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        tree_len = len(preorder)
        if tree_len == 0:
            return None

        self.preorder = preorder
        self.inorder = inorder

        self.mapping = {val: index for index, val in enumerate(inorder)}

        return self.rec(0, tree_len, 0, tree_len)

    def rec(self, istart, iend, pstart, pend):

        if istart >= iend or pstart >= pend:
            return None

        root_val = self.preorder[pstart]
        root_index = self.mapping[root_val]
        root = TreeNode(val=root_val)

        diff = root_index - istart

        root.left = self.rec(istart, root_index, pstart + 1, pstart + diff + 1)
        root.right = self.rec(root_index + 1, iend, pstart + diff + 1, pend)

        return root
