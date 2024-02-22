class Solution:
    def isValid(self, s: str) -> bool:
        x={')':'(',']':'[','}':'{'}

        stack=[]

        for i in s:
            if i in x.values(): 
                stack.append(i)
            elif stack and stack[-1] == x[i]:
                stack.pop()
            else:
                return False
        return stack == []

        
        
        
 
       
        
        