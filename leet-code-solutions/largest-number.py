class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        cnt = 0
        s = ""
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == 0 and nums[j] == 0:
                    cnt += 1
            if cnt == len(nums):
                return str(0)

        
        for i in range(len(nums)):
            for j in range(len(nums)):
                
                if (str(nums[i]) + str(nums[j])) > (str(nums[j]) + str(nums[i])):
                    nums[i], nums[j] = nums[j], nums[i]
        for i in range(len(nums)):
            s += str(nums[i])

        return s
       

            
        


        