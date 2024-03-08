class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort(reverse = True)
        l = 0
        r = len(citations) - 1
        if len(citations) == 1 and citations[0] == 0:
            return 0
        elif len(citations) == 1 and citations[0] != 0:
            return 1
        # print(citations)
        while l <= r:
            mid = (l+r)//2

            if (citations[mid]) - (mid+1) < 0:
                r = mid - 1
            
            elif (citations[mid]) - (mid+1) > 0:
                if r == mid:
                    return r + 1
                else:
                    l =  mid + 1 
            else:
                return mid + 1
        return mid













        