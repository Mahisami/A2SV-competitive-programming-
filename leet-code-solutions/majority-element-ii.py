class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = []
        d = {}
        N = len(nums)//3
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1

        for key, value in d.items():
            if value > N:
                out.append(key)

        return out
