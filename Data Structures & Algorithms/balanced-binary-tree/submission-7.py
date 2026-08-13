# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        node = root
        heights = {None: 0}
        stack = [(root, False)]

        while stack:
            node, processed = stack.pop()
            if not node:
                continue
            
            if processed:
                left_h = heights[node.left]
                right_h = heights[node.right]
                if abs(left_h - right_h) > 1:
                    return False
                heights[node] = 1 + max(left_h, right_h)
            else:
                stack.append((node, True))
                stack.append((node.left, False))
                stack.append((node.right, False))
        
        return True

            
        
        