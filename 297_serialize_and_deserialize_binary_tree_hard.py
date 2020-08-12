# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    """
    Description:
        Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
        Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
        Example:

        You may serialize the following tree:

            1
           / \
          2   3
             / \
            4   5

        as "[1,2,3,null,null,4,5]"
        Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

        Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
    Idea:
        Use stack to serialize and stack plus index to deserialize. In deserialization every node will have two
        items based on index. Since we have a binary tree there are always two items for every node.
        So data[index] - is left, data[index+1] is right
    Complexity:
        Time: O(n)
        Space: O(n)

    """

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return ""

        res = []
        stack = [root]
        while stack:
            node = stack.pop(0)
            if node:
                stack.append(node.left)
                stack.append(node.right)

            res.append(str(node.val) if node else "#")
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(',')
        root = TreeNode(int(data[0]))
        stack = [root]
        index = 1
        while stack:
            node = stack.pop(0)

            if data[index] != "#":
                node.left = TreeNode(int(data[index]))
                stack.append(node.left)
            index += 1

            if data[index] != "#":
                node.right = TreeNode(int(data[index]))
                stack.append(node.right)
            index += 1

        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
