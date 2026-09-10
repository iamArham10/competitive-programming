# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        result = []
        queue.append(root)
        while len(queue) > 0:
            current_level = []
            new_queue = deque()
            for node in queue:
                if (node):
                    new_queue.append(node.left)
                    new_queue.append(node.right)
                    current_level.append(node.val)
            queue = new_queue
            if len(current_level) > 0:
                result.append(current_level)

        return result
            
        

        