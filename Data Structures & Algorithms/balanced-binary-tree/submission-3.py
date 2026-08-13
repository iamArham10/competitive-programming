# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(node):
            if not node:
                return [0, True]
            
            leftHeight, isLeftBalanced = helper(node.left)
            rightHeight, isRightBalanced = helper(node.right)
            condition = abs(rightHeight - leftHeight) < 2

            return [1 + max(leftHeight, rightHeight), condition and isLeftBalanced and isRightBalanced]
        
        return helper(root)[1]
        
        