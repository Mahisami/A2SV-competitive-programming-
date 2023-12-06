class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i] > nums[i+1]:
                if i-1 >= 0 and nums[i+1] < nums[i-1]:
                    nums[i+1] = nums[i]
                else:
                    nums[i] = nums[i+1]
                count += 1        
        return count <= 1