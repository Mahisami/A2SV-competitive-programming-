class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x

        while True:
            mid = (l+r) // 2

            if mid ** 2 <= x and (mid+1) ** 2 > x:
                return mid

            elif (mid ** 2) > x and (mid + 1) ** 2 > x:
                r = mid - 1
            else:
                l= mid + 1
        # return r









 