class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        l = 0
        r = n
        out = []
       
        while r <= len(nums)-1:
            out.append(nums[l])
            out.append(nums[r])
            l+=1
            r+=1
        return out
        

            

        