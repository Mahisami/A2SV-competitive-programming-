class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        cnt = 0
        while True:
            if target == 1:
                return cnt
            if target % 2 == 0:
                if maxDoubles != 0:
                    target //= 2
                    cnt += 1
                    maxDoubles -= 1
                else:
                    return cnt +(target - 1)
            else:
                cnt += 1
                target -= 1
            
        return cnt

        