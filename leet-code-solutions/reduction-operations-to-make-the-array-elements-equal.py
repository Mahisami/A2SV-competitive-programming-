class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = {}
        
        ss =set(nums)
        li = list(ss)
        li.sort()

        for i in range(len(li)):
            if li[i] not in s:
                s[li[i]] = i
           
        cnt = 0
        
        for i in range(len(nums)):
            cnt += s[nums[i]]
         
        return cnt


