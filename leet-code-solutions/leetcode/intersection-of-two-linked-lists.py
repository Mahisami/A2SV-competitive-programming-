# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        listA = headA
        listB = headB
        visited = set()

        while listA:
            visited.add(listA)
            listA = listA.next

        while listB:
            if listB in visited:
                return listB
            listB = listB.next

        return None 
