# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # fast and slow
        # find mid
        # reverse second half
        # go one by one interchanging first and second halves

        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
            
        mid = s

        second_half = mid

        prev = None

        while second_half:
            second_half.next, prev, second_half = prev, second_half, second_half.next

        l1 = head
        l2 = prev

        dummy = ListNode(-1, l1)
        while l1.next and l2.next:
            l1.next, l2.next, l1, l2 = l2, l1.next, l1.next, l2.next
        

        
