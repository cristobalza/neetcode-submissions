# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        minheap = []

        for lst in lists:
            curr = lst
            while curr:
                heapq.heappush(minheap, curr.val)
                curr = curr.next

        dummy = ListNode(-1)
        curr = dummy

        while minheap:
            val = heapq.heappop(minheap)
            node = ListNode(val)
            curr.next = node
            curr = curr.next

        return dummy.next