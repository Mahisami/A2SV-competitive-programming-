class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        out = ""
        i = 0
        
        while i < len(s):
            out += s[i:i+k][::-1]
            out += s[k+i:i+k+k]
            i += k+k
        return out
           
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
  