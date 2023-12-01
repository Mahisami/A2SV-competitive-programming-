class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        output = 0
        n = len(salary)-1
        for i in range(1,n):
            output += salary[i]
           
            
        return output/(n-1)
            

        