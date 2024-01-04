class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        l = 1
        cnt = 1
        while l < len(nums):
            if nums[l] != nums[l-1]:
                nums[cnt] = nums[l]
                cnt += 1
                l += 1
            else:
                l += 1
         
          
        return cnt
                
        