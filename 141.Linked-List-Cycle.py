# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr=head
        arr=[]
        if not head or not head.next:
            return False
        while id(curr) not in arr and curr.next:
            arr.append(id(curr))
            curr=curr.next
            if curr.next is None:
                return False
            
        return True
