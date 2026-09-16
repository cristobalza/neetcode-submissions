# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # bfs

        if not root:
            return 0

        q = collections.deque()
        q.append(root)

        res = 0

        while q:

            res += 1

            size_q = len(q)

            for _ in range(size_q):

                node = q.popleft()

                if node and node.left:
                    q.append(node.left)

                if node and node.right:
                    q.append(node.right)

        return res
