class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        oddHead = head 
        odd = oddHead
        evenHead = head.next
        even = evenHead

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
            odd.next = evenHead

        return oddHead
