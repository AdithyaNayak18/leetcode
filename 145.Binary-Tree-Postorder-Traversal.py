# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node,arr):
            if node is None:
                return
            
            dfs(node.left,arr)
            dfs(node.right,arr)
            arr.append(node.val)
            
        arr=[]
        dfs(root,arr)
        return arr
        
