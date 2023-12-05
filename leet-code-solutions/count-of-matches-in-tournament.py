class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
       
        while n!=1:
            ans += n//2
            if n%2 == 0 :
                n = n//2
            else:
                n = (n//2) + 1
        return ans