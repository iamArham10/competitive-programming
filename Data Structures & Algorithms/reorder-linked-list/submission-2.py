class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Find middle
        single = head
        double = head

        while double and double.next:
            single = single.next
            double = double.next.next

        # Reverse second half
        reverseHead = single.next
        single.next = None

        prev = None

        while reverseHead:
            next_node = reverseHead.next
            reverseHead.next = prev
            prev = reverseHead
            reverseHead = next_node

        # Merge the two halves
        while head and prev:
            head_next = head.next
            prev_next = prev.next

            head.next = prev
            prev.next = head_next

            head = head_next
            prev = prev_next

        
        