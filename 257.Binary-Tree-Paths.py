# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node,s,arr):
            if not node:
                return
            if not node.right and not node.left:
                s+=f"{node.val}"
                arr.append(s)
                return
            s+=f"{node.val}->"
            dfs(node.left,s,arr)
            dfs(node.right,s,arr)
        arr=[]
        s=""
        dfs(root,s,arr)
        return arr

        
