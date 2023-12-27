class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        add = 0 
        n = len(mat)
        for r in range(n):
            add += mat[r][r]
            add += mat[r][n - 1 - r]
        if n % 2 == 1:
            add -= mat[n//2][n//2]
        return add