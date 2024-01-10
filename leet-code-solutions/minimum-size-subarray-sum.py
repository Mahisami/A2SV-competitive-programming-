class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = 0
        min_val = float("inf")
        start = 0
        for i in range(len(nums)):
            result += nums[i]
            
            while result >= target:
                min_val = min(min_val, i - start + 1)
                result -= nums[start]
                start += 1
                
        return 0 if min_val == float('inf') else min_val
    

    

      

    

         
                
                
                
                
                
           
            
        
        