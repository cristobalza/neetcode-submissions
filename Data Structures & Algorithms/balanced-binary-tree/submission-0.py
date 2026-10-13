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

        # bfs

        q = collections.deque()
        q.append((root, 1))

        min_h = 1

        while q:

            children = len(q)

            for _ in range(children):

                node, h = q.popleft()

                if h - min_h > 1:
                    return False

                # update min_h
                if not node.left and not node.right:
                    min_h = h

                if node.left:
                    q.append((node.left, h + 1))

                if node.right:
                    q.append((node.right, h + 1))

        return True

                
        