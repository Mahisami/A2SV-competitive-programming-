class Solution:
    def countGoodNumbers(self, n: int) -> int:
        x = 1000000007
        return (pow(5,(n+1)//2,x) * pow(4,n//2,x)) % x
        