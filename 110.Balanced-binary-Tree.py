# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def calc_depth(node):
            if not node:
                return 0
            
            left = calc_depth(node.left)
            right = calc_depth(node.right)

            if abs(left - right) > 1:
                return -1
            
            if min(left,right) == -1:
                return -1

            return 1 + max(left, right)
        
        return calc_depth(root) != -1
      
