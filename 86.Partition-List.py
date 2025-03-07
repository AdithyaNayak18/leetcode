# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left,right=ListNode(),ListNode() #First node is dummy node , thatst why first     element is in .next
        lt,rt=left,right
    
        while head:
            if head.val<x:
                lt.next=head
                lt=lt.next
            else:
                rt.next=head
                rt=rt.next
            head=head.next
        
        lt.next=right.next
        rt.next=None
        return left.next
