class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        nums = num//3
        if num % 3 !=0:
            return []
        
        x = []
        x.append(nums-1)
        x.append(nums)
        x.append(nums+1)

        return x
        
        