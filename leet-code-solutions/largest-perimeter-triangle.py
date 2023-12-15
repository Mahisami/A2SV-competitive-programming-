class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        output = 0

        nums.sort()
        right = len(nums) - 1
        while right >= 2:
            if nums[right] < nums[right - 1] + nums[right - 2]:
                return nums[right] + nums[right - 1] + nums[right - 2]
            
            right -= 1
        return 0
        
        
        
        
        
        