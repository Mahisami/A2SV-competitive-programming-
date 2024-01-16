class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefsum = []
        out = 0
        
        for i in range(len(nums)):
            out += nums[i]
            prefsum.append(out)
        return prefsum
            
