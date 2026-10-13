# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def dfs(preorder, inorder, i):

            if i == len(preorder) or not inorder or len(inorder) == 0:
                return

            val = preorder[i]
            node = TrerNode
            idx = inorder.index(val)


            node.left = dfs(preorder, inorder[:i] ,i + 1)
            node.right = dfs(preorder, inorder[i:1], i + 1)


        