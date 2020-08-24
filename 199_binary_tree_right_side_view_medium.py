# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Description:
        Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
        Example:
        Input: [1,2,3,null,5,null,4]
        Output: [1, 3, 4]
        Explanation:

           1            <---
         /   \
        2     3         <---
         \     \
          5     4       <---
    Idea:
        A: Use queue to get all items from level
        B: Use queue and also pass current level. We start from right, and compare the current level with the length of result
    Complexity:
        A:
            Time: O(N)
            Space: O(N)
        B:
            Time: O(N)
            Space: O(N)
                
    """
    def rightSideView(self, root: TreeNode) -> List[int]:
#         if not root:
#             return []
        
#         queue = [[root]]
#         res = []
#         while queue:
#             level = queue.pop(0)
#             new_level = []
#             for node in level:
#                 if node.left:
#                     new_level.append(node.left)
#                 if node.right:
#                     new_level.append(node.right)
#             if new_level:   
#                 queue.append(new_level)
#                 res.append(new_level)
#         final_res = [root.val]
#         for entry in res:
#             final_res.append(entry[-1].val)
#         return final_res

        if not root:
            return []

        res = []
        queue = [(root, 0)]

        while queue:
            node, level = queue.pop(0)

            if node:
                if len(res) == level:
                    res.append(node.val)
                queue.append((node.right, level + 1))
                queue.append((node.left, level + 1))
        return res
