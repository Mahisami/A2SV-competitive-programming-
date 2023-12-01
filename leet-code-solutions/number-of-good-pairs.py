class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
    
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    count += 1
                
        return count
        # l = 0
        # r = 1
        # count = 0
        # nums.sort()
        # while r < len(nums):
        #     if nums[l] == nums[r]:
        #         count += r -
        #         r+=1
        #     else:
        #         l += 1
        #         r = l +1

          
        # return count


                    
        