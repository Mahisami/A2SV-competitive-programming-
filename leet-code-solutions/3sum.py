class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        l = 0
        result = []
        
        while l < len(nums) - 2:
            if l > 0 and nums[l] == nums[l - 1]:
                l += 1
                continue
                
            r = l + 1
            s = len(nums) - 1
            
            while r < s:
                curSum = nums[l] + nums[r] + nums[s]
                
                if curSum == 0:
                    result.append([nums[l],nums[r],nums[s]])
                    
                    while r < s and nums[r] == nums[r + 1]:
                        r += 1
                    while r < s and nums[s] == nums[s - 1]:
                        s -= 1
                        
                    r += 1
                    s -= 1
                    
                elif curSum < 0:
                    r += 1
                else:
                    s -= 1
            l += 1
        return result
                
                
        