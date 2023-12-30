class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        total = 0
        cnt = 0

        for cost in costs:
            total += cost
            if total > coins:
                break
            cnt += 1

        return cnt
