# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    Description:
        Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
        According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
        Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
        Example 1:

        Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
        Output: 3
        Explanation: The LCA of nodes 5 and 1 is 3.

        Example 2:

        Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
        Output: 5
        Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

        Note:

        All of the nodes' values will be unique.
        p and q are different and both values will exist in the binary tree.
    Idea:
        Traverse the tree via stack while both p and q are not in the hashtable
        record all the ancestors of any node into set.
        Iterate over ancestors of another node until its parent is not in ancestors
    Complexity:
        Time: O(n)
        Space: O(n)
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        mapping = {root: None}

        stack = [root]

        while p not in mapping or q not in mapping:
            node = stack.pop()

            if node.left:
                mapping[node.left] = node
                stack.append(node.left)

            if node.right:
                mapping[node.right] = node
                stack.append(node.right)

        ancestors = set()

        while p:
            ancestors.add(p)
            p = mapping[p]

        while q:
            if q in ancestors:
                return q
            q = mapping[q]
