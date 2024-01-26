# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lhead = less = None
        ghead = greater = None

        while head:
            if head.val < x:
                if less is None:
                    lhead = less = head
                else:
                    less.next = head
                    less = less.next
            else:
                if greater is None:
                    ghead = greater = head
                else:
                    greater.next = head
                    greater = greater.next

            head = head.next

        if less:
            less.next = ghead
        else:
            return ghead  

        if greater:
            greater.next = None

        return lhead
