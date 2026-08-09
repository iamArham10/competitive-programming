# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        node1 = headA
        node2 = headB

        while (node1 != node2):
            if not node1 and node2:
                node1 = headB
            if not node2 and node1:
                node2 = headA
            node1 = node1.next
            node2 = node2.next
            
        return node1
        