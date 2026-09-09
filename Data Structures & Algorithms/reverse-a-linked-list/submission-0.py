# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ 
         head = [0,1,2,3]
                p c

            0<- 1 <- 2 <- 3
                           p   c
        c.next = p
        p = c
        c = c.next
        """
        p, c = None, head

        while c:
            c.next, p, c = p, c, c.next

        return p