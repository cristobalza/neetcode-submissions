# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, prev, isleft):
            if not node:
                return True

            if isleft:
                if prev and node.val >= prev.val:
                    return False

            else:
                if prev and node.val <= prev.val:
                    return False

            left = dfs(node.left, node, True)
            right = dfs(node.right, node, False)

            return left and right


        return dfs(root, None, True) and dfs(root, None, False)



            

        