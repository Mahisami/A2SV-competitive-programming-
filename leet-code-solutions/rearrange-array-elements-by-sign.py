class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        left = 0 
        positive = []
        negative = []
        out = []
        for num in range(len(nums)):
            
            if nums[num] > 0 :
                positive.append(nums[num])
            else:
                negative.append(nums[num])
       
        while left < len(positive) and left < len(negative):
            out.append(positive[left])
            out.append(negative[left])
            left += 1
           
        return out
            


        