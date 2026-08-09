# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def check(self, root1, root2):
        if not root2 and not root1:
            return True

        if not root1 or not root2:
            return False

        if root1.val != root2.val:
            return False
        
        return self.check(root1.left, root2.left) and self.check(root1.right, root2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        
        return self.check(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            
        