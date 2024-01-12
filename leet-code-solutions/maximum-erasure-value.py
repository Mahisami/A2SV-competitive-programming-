class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        d = defaultdict(int)
        summ = 0
        start = 0
        end = 0
        max_val = 0
        while end <= len(nums)-1:
            d[nums[end]] += 1
            while d[nums[end]] > 1:
                d[nums[start]] -= 1
                summ -= nums[start]
                start += 1
            summ += nums[end]
            max_val = max(max_val, summ)
            end += 1


            
        return max_val
                
                
                
                
            
            
            
            
            
            
            
            
            
            
            
        