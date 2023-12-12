class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        my_counter = Counter(arr)

        max_key = max(my_counter, key = my_counter.get)

       
        return max_key

            
        