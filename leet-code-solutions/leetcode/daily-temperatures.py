class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, x in enumerate(temperatures):
            while stack and x > stack[-1][0]:
                stacki, stackx = stack.pop()
                res[stackx] = i - stackx
             
            stack.append([x, i]) 
        return res

        
        
