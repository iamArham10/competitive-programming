# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr_sum = 0
        node = root
        stack = []

        while stack or node:
            while node:
                stack.append(node)
                node = node.right
            node = stack.pop()
            curr_sum += node.val
            node.val = curr_sum
            node = node.left
        
        return root






        