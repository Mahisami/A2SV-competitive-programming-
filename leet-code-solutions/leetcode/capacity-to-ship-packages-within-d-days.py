class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def helper(mid):

            capac = mid
            cnt = 1

            for weight in weights:
                if weight > capac:

                    if cnt >= days:
                        return True
                    cnt += 1
                    capac = mid

                capac -= weight

            return False

        l = max(weights)
        r = math.ceil(len(weights) / days) * max(weights)

        while l < r:
            mid = (l + r) // 2

            if helper(mid):
                l = mid + 1
            else:
                r = mid

        return l
