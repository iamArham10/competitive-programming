# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        curr = float("-inf")
        def helper(node: Optional[TreeNode]):
            nonlocal curr
            if not node:
                return True;
            isLeft = helper(node.left)
            if node.val <= curr:
                return False
            curr = node.val
            return isLeft and helper(node.right)
        return helper(root)


        