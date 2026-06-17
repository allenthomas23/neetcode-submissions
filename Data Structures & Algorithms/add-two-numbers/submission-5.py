# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        dummy =res
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum1 = val1 + val2 +carry
            if sum1 >=10:
                carry = 1
                sum1 -=10
            else:
                carry = 0
            res.next = ListNode(sum1)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            res = res.next

        if l1:
            res.next = l1
        elif l2:
            res.next = l2
        return dummy.next