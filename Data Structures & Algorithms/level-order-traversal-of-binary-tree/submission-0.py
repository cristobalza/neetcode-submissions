# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        q = collections.deque()
        q.append(root)

        res = []

        while q:

            subset = []

            q_size = len(q)

            for _ in range(q_size):

                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

                subset.append(node.val)

            res.append(subset)

        return res

        