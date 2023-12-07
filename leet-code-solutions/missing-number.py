class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        d = {}
        output = -1
        for i in range(len(nums)):
            d[i] = nums[i]
            if d[i] != i:
                output = i
                break
            
        return output  if output != -1 else len(nums)
