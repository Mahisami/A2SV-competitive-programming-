class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x = []
        for i in range(0, len(nums), 2):
            x += [nums[i+1]] * nums[i]
        return x





