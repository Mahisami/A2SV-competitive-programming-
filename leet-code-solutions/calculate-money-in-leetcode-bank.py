class Solution:
    def totalMoney(self, n: int) -> int:
        # a = n // 7
        # b = n % 7
        # return a * 28 + 7 * (a - 1) * a // 2 + (a + 1 + a + b) * b // 2
        out = 0
        i = 1 
        while n > 7 :
            out += sum(range(i, 7+i))
            i += 1
            n -= 7
        out += sum(range(i, n+i))
        return out 
            


       