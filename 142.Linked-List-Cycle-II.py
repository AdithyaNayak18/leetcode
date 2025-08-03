# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d=dict()
        curr=head
        if not head or not head.next:
            return None
        c=0
        while id(curr) not in d.keys() and curr.next:
            d[id(curr)]=c
            c+=1
            curr=curr.next
            if curr.next is None:
                return None
        return curr if c>0 else curr.next
        
