class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        max_val = 0
        length = len(blocks)
      
        s = 0
        l = k - 1
        
        for i in range(k - 1, length):
            c = Counter(blocks[s: l + 1])
            print(c)
            max_val = max(c['B'], max_val)
            l += 1
            s += 1
            
            
        return k - max_val
            
                
                
                
                
        
        
        
        