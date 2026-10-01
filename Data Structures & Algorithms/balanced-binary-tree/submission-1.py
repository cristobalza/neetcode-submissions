# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """

                    1 h:1

            2. h:2             3 h:2

                         4 h:3

                  5 h:4


        """
        if not root: 
            return True

        def dfs(node):

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) > 1:
                return float("inf")

            return max(left, right) + 1

        res = dfs(root) 

        return True if res != float("inf") else False

                
        