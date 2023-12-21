class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        li = []
   
        s = [str(i) for i in digits]
        res = int("".join(s)) + 1
        out = [int(i) for i in str(res)]
        for i in range(len(out)):
            li.append(out[i])
        return li
            
        
            
      
        
       

        