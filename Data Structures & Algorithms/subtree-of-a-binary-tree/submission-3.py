# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot:
            return not root

        def dfs(node, subNode):
            if not node:
                return False

            if node.val == subNode.val:
                if check_dfs(node, subNode):
                    return True

            return dfs(node.left, subNode) or dfs(node.right, subNode)

        def check_dfs(node, subNode):
            if not node and not subNode:
                return True

            if (not node or not subNode) or (node.val != subNode.val):
                return False

            return check_dfs(node.left, subNode.left) and check_dfs(node.right, subNode.right)

        return dfs(root, subRoot)
        
        