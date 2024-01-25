# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        
        
        straight =deque()
        revers = deque()
        while head:
            straight.append(head.val)
            revers.appendleft(head.val)
            head = head.next
        
        return straight == revers
