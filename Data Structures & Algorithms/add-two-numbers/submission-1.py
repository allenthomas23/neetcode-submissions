# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i = 1
        curr = l1
        sum1 = 0
        while(curr):
            sum1 += i * curr.val
            i*=10
            curr = curr.next
        curr = l2
        j=1
        sum2 = 0
        while(curr):
            sum2 += j * curr.val
            j*=10
            curr = curr.next
        new = ListNode()
        curr = new
        total = sum1 + sum2
        #example 807 -> 7>0>8
        if total == 0:
            return ListNode(0)
        while(total > 0):
            digit = total % 10
            total = total // 10 
            curr.next = ListNode(digit)
            curr = curr.next
        return new.next
                
        
        

            