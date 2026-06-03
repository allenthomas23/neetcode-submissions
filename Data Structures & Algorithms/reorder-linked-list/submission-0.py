# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        t = head
        nodes = []
        while(t):
            nodes.append(t)
            t = t.next
        i = 0
        j = len(nodes) -1 
        while i<j:
            if i == j:
                nodes[i].next = nodes[j]
            else:
                nodes[i].next = nodes[j]
                i+=1
                nodes[j].next = nodes[i]
                j-=1
        nodes[i].next = None
        return


            

