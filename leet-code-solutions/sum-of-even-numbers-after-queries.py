class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
       result = []
       summ = 0
       for i in range(len(nums)):
           if nums[i] % 2 == 0:
               summ += nums[i]
       for i in range(len(queries)):
            val, val1 = queries[i]
            if nums[val1] % 2 == 0:
                summ -= nums[val1]
            nums[val1] += val
            if nums[val1] % 2 == 0:
                summ += nums[val1]
            result.append(summ)
       return result

            

        


                
         
            
        

        