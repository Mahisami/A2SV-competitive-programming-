class Solution:
    def balancedString(self, s: str) -> int:
        count = collections.Counter(s)
        l,res = 0, len(s)
        for end in range(len(s)):
            count[s[end]] -= 1
            while l < len(s) and all( len(s)//4 >= count[j] for j in "QWER"):
                res = min(res,end - l+1)
                count[s[l]] += 1
                l += 1
        return res

        
        
        