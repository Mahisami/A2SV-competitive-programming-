class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        elif n == 1:
            return x
        ans = self.myPow(x,abs(n//2))
        if n < 0:
            return 1/(self.myPow(x,abs(n)))

        
        if n % 2 == 0:

            return ans * ans

        else:
            return x*ans * ans
            
        
      
     
        