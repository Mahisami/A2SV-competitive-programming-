class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1 and k == 1: return 0

        mid = pow(2,n-1) // 2
       
        x = 0
        if k <= mid:
            x = self.kthGrammar(n-1,k)
        else:
            x = 1 ^ self.kthGrammar(n-1,k-mid)
        return x
