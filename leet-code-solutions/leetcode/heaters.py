class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        maxx = 0
        heaters.sort()
        for i in houses:
            l = bisect_left(heaters,i)
            lr = i - heaters[l-1] if l > 0 else float("inf")

            rr = heaters[l] - i if l < len(heaters) else float("inf")

            minn = min(lr, rr)

            maxx= max(maxx, minn)
        return maxx
















        # for i in houses:
        #     l = bisect_left(heaters, i)
        #     lr = i - heaters[l-1] if l > 0 else float("inf")

        #     rr = heaters[l] - i if l < len(heaters) else float("inf")

        #     minn = min(lr, rr)

        #     maxx= max(maxx, minn)
        # return maxx 
  

    
   