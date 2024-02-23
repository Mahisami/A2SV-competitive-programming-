from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        if rows == 0:
            return
        cols = len(matrix[0])
        if cols == 0:
            return

        summ = [[0] * (cols + 1) for _ in range(rows + 1)]

        for i in range(rows):
            for j in range(cols):
                row = i + 1
                col = j + 1
                summ[row][col] = (
                    summ[row][col - 1]
                    - summ[row - 1][col - 1]
                    + summ[row - 1][col]
                    + matrix[i][j]
                )

        self.summ = summ

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        summ = self.summ
        return (
            summ[row2 + 1][col2 + 1]
            - summ[row2 + 1][col1]
            - summ[row1][col2 + 1]
            + summ[row1][col1]
        )
