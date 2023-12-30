class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        cnt = 1
        piles.sort(reverse = True)
        output = 0
        
        endLine = 2* len(piles) // 3
        
        while cnt < endLine:
            output += piles[cnt]
            cnt += 2
        return output
            
            