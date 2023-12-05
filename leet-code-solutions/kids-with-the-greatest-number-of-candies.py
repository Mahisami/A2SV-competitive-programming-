class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_one = 0
        x = 0
        out = []
        for i in range(len(candies)):
            max_one = max(max_one,candies[i])
        for i in range(len(candies)):
            x = candies[i] + extraCandies
            if x < max_one:
                out.append(False)        
            else:
                out.append(True)
        return out
       
        