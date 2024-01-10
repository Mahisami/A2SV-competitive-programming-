class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_start = 0
        max_val = float("-inf")
        window_sum = 0
        
        for i in range(len(nums)):
            window_sum += nums[i]
            
            if i >= k - 1:
                max_val = max(max_val, (window_sum/k))
                window_sum -= nums[window_start]
                window_start += 1
        return max_val
            
        