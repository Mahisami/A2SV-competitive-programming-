# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = 0
        new = head
        li = []
        while new:
            li.append(new.val)
            new = new.next
        li.sort()
        curr = head
        i = 0
        while curr:
            curr.val = li[i]
            curr = curr.next
            i+=1
        return head
            
            
            
        