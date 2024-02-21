class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        grid = [[0]*len(colSum) for _ in range(len(rowSum))]
        # print(grid)
        
        for r in range(len(rowSum)):
            for c in range(len(colSum)):
                minVal = min(rowSum[r],colSum[c])
                grid[r][c] = minVal
                rowSum[r] -= minVal
                colSum[c] -= minVal
        return grid



        