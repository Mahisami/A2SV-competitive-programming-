class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: -abs(x[0] - x[1]))
        total = 0
        A = B = len(costs)/2

        for i, j in costs:
            if B == 0 or (A > 0 and i <= j):
                total += i
                A -= 1
            else:
                total += j
                B -= 1
        return total
