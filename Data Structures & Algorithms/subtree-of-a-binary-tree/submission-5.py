# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        
        def dfs(node, sub):

            if not node:
                return False

            if node.val == sub.val:

                is_same = sub_dfs(node, sub)

                if is_same:
                    return True

            l = dfs(node.left, sub)
            r = dfs(node.right, sub)

            return l or r


        def sub_dfs(node, sub):
            if not node and not sub:
                return True

            if (not node or not sub) or (node.val != sub.val):
                return False

            return sub_dfs(node.left, sub.left) and sub_dfs(node.right, sub.right)

        return dfs(root, subRoot)

        
        