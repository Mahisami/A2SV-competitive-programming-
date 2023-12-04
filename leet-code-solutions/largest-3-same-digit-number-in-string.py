class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        d = ["000", "111", "222", "333", "444", "555", "666", "777", "888", "999"]
        
        nums = -1

        for i in range(len(d)):
           
            if d[i] in num:
                nums = max(nums, i)
        if nums != -1:
            return d[nums]
        else:
            return ""

