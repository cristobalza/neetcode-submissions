# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """

        root=[3,3,null,4,2]


                3

        3

4.         2

        """
        if not root:
            return 0


        def dfs(node, max_ancestor):
            if not node:
                return 0

            res = 1 if node.val >= max_ancestor else 0

            max_ancestor = max(node.val, max_ancestor)

            left = dfs(node.left, max_ancestor)
            right = dfs(node.right, max_ancestor)

            return res + left + right 


        return dfs(root, float("-inf"))


        