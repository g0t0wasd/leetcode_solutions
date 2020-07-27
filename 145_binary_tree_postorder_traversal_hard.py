# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Description:
        Given a binary tree, return the postorder traversal of its nodes' values.
        Example:
        Input: [1,null,2,3]
           1
            \
             2
            /
           3

        Output: [3,2,1]
    Idea:
        Use BFS and then rotate the result or insert the nodes into begining of the result
    Complexity:
        Time: O(n)
        Space: O(n)
    """
    def another_postorderTraversal(self, root: TreeNode) -> List[int]:
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []

        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.insert(0, node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
            Idea with double adding
        """
        ret = []
        if not root:
            return ret
        st = [root] * 2
        while st:
            cur = st.pop()
            if st and st[-1] is cur:
                if cur.right:
                    st += [cur.right] * 2
                if cur.left:
                    st += [cur.left] * 2
            else:
                ret.append(cur.val)
        return ret
