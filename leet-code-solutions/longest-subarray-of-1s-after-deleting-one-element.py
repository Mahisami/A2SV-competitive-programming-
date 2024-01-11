class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cnt = 0
        start = 0
        end = 0
        max_len = 0
        for i in range(len(nums)):

            if nums[i] == 0:
                cnt += 1
            end += 1
            
            while cnt > 1:
                if nums[start] == 0:
                    nums[start] = 1
                    cnt -= 1
                start += 1
            max_len = max(max_len, end-start-1)
        return max_len

      
            



            
            
                
        