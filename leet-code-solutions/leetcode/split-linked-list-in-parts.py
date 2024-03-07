class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cnt = 0
        temp = head
        while temp:
            cnt += 1
            temp = temp.next
        print(cnt)

        val = cnt // k
        remainder = cnt % k
        print(val,remainder)

        result = []

        current = head
        for i in range(k):
            size = val + (1 if i < remainder else 0)
            result.append(current)

            for j in range(size-1):
                if current:
                    current = current.next

            if current:
                temp = current.next
                current.next = None
                current = temp

        return result
