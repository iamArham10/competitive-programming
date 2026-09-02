# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def helper(node: TreeNode, curMax: int) -> int:

            if not node:
                return 0
            
            res = 1 if node.val >= curMax else 0
            curMax = max(node.val, curMax)
            left = helper(node.left, curMax)
            right = helper(node.right, curMax)
            return res + left + right
        
        return helper(root, root.val)