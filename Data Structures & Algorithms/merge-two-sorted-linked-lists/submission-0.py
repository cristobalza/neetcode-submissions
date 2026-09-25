# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 or not list2:
            return list1 or list2

        dummy = ListNode(-1)

        if list1.val < list2.val:
            dummy.next = list1
        else:
            dummy.next = list2

        c1, c2 = list1, list2
        curr = dummy.next

        while c1 and c2:
            if c1.val < c2.val:
                curr.next, c1 = c1, c1.next
            else:
                curr.next, c2 = c2, c2.next

            curr = curr.next

        if not c2:
            curr.next = c1
        else:
            curr.next = c2

        return dummy.next

        