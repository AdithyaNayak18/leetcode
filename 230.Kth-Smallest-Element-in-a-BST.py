# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.c=0
        self.ans=-1
        def inorder(node):
            if not node or self.ans!=-1:
                return 
            inorder(node.left)
            self.c+=1
            if self.c==k:
                self.ans=node.val
                return 
            inorder(node.right)
            
        inorder(root)
        return self.ans
            
