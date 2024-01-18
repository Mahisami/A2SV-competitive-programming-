class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        window =n-k
        cursum = sum(cardPoints[:window])
        min_val = cursum

        for i in range(window, n):
            cursum += cardPoints[i] - cardPoints[i - window]
            min_val = min(min_val, cursum)
        total = total - min_val
        return total


        