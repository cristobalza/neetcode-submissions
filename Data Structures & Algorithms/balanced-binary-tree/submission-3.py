# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node, h):
            if not node:
                return True, h

            left, l_h = dfs(node.left, h + 1)
            right, r_h = dfs(node.right, h + 1)

            if abs(l_h - r_h) > 1:
                return False, h

            return left and right, max(l_h, r_h, h)
            
        
        res, _ = dfs(root, 0)

        return res
        