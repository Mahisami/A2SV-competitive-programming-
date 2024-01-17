class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        y = nums[len(nums)-1]
        right = [y]
        n = len(nums)
        x = nums[0]
        left = [x]
        ans = []

        for i in range(1,n):
            x *= nums[i]
            left.append(x)

          
        for i in range(n-2, -1, -1):
            y *= nums[i]    
            right.append(y)
        right.reverse()

        for i in range(len(nums)):
            if i == 0:
                ans.append(right[i+1])
            elif i == n-1:
                ans.append(left[i-1])
            else:
                ans.append(right[i+1] * left[i-1])

        
        return ans
            
            
            
            
      
