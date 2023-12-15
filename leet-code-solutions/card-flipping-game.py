class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        
        s = set()
        res = 3000

        for f, b in zip(fronts, backs):
            if f == b:
                s.add(f)
               
        for f in fronts:
            if f not in s:
                res = min(res, f)
      
        for b in backs:
            if b not in s:
                res = min(res, b)
    

        return res if res != 3000 else 0 
            

                    
        
       

            
            




        