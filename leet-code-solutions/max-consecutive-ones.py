class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        l = 0
        max_count = 0
        while l <= len(nums)-1:
            if nums[l] == 1:
                count += 1
                max_count = max(max_count, count)
                l+=1
            else:
                l += 1
                count = 0
        return max_count
        