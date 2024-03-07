class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        def cal(target):
            res = 0
            for i in piles:
                res += ceil(i/target)
            return res <= h
        
        while l <= r:
            mid = (l+r)//2
            if cal(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l

        
        