# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    m=float('-inf')
    def findmax(self,root):
        if not root:
            return 0
        l=self.findmax(root.left)
        r=self.findmax(root.right)
        if l<=0:
            l=0
        if r<=0:
            r=0
        
        self.m=max(self.m,l+r+root.val)
        return max(l,r)+root.val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.findmax(root)
        return self.m
