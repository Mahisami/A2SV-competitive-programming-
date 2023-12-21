class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        cnt = 0
        # l = 0
        # r = 1
        for num in range(len(nums)):
            for j in range(num):
                if nums[num] == nums[j] and (num*j)%k == 0:
                    cnt += 1
        return cnt
                
        
#         while r <= len(nums)-1:
#             if nums[l] == nums[r] and (l*r)%k == 0:
#                 cnt += 1
#                 r += 1
#             l += 1
          
#         print(cnt)
        
                
            
        