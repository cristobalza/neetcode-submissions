# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def get_num_str(l: Optional[ListNode]) -> str:
            num_str = ""
            curr = l

            while curr:
                num_str += str(curr.val)

                curr = curr.next

            return num_str

        num1_str = get_num_str(l1)[::-1]
        num2_str = get_num_str(l2)[::-1]

        num_str = str(int(num1_str) + int(num2_str))[::-1]

        dummy = ListNode(-1)
        curr = dummy
        idx = 0

        while idx < len(num_str):
            node = ListNode(int(num_str[idx]))

            curr.next = node

            curr = curr.next

            idx += 1

        return dummy.next



