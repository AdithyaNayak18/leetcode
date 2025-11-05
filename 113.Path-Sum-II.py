# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        self.dfs(root, targetSum, 0, [], res)
        return res

    def dfs(self, node, targetSum, curr_sum, curr_path, res):
        # 1. Base case: If the node is None, this path is invalid.
        if not node:
            return

        # 2. Update the current sum and path with this node's value
        curr_sum += node.val
        # Create a NEW list by concatenating, instead of using .append()
        curr_path = curr_path + [node.val] 

        # 3. Check if it's a leaf node (no left and no right child)
        if not node.left and not node.right:
            # 4. If it's a leaf, check if the path sum is correct
            if curr_sum == targetSum:
                res.append(curr_path)
            # 5. Whether the sum matches or not, stop recursing down this branch
            return

        # 6. If not a leaf, continue recursing on children
        # Note: We use self.dfs and pass the updated curr_sum and curr_path
        self.dfs(node.left, targetSum, curr_sum, curr_path, res)
        self.dfs(node.right, targetSum, curr_sum, curr_path, res)
