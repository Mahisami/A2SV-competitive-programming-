class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s ) < 2:
            return ""
        
        longest = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                sub = s[i:j+1]
                nice = True
                
                for k in sub:
                
                    if k.upper() not in sub or k.lower() not in sub:
                        nice = False
                        break
                if nice and len(sub) > len(longest):
                    longest = sub
                    
        return longest
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        