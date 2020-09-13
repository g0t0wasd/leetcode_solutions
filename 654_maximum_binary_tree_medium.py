# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Description:
        Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

        The root is the maximum number in the array.
            The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
            The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
        Construct the maximum tree by the given array and output the root node of this tree.

        Example 1:
        Input: [3,2,1,6,0,5]
        Output: return the tree root node representing the following tree:

              6
            /   \
           3     5
            \    /
             2  0
               \
                1
        Note:
        The size of the given array will be in the range [1,1000].
    Idea:
        A: recursive
        B: construct stack, while iterating over the array. This way we allways will know which item is to the left / right
            of current node
    Complexity:
        A:
            Time: O(n**2)
            Space: O(n) ?
        B:
            Time: O(n)
            Space: O(n)
    """
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
#         if not nums:
#             return None
#         max_val = max(nums)
#         max_index = nums.index(max_val)
#         root = TreeNode(val=max_val)
#         root.left = self.constructMaximumBinaryTree(nums[:max_index])
#         root.right = self.constructMaximumBinaryTree(nums[max_index+1:])
#         return root

        if not nums:
            return None
        stack = []
        for num in nums:
            left_candidate = None
            node = TreeNode(num)
            while stack and stack[-1].val < num:
                left_candidate = stack.pop()

            node.left = left_candidate

            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
