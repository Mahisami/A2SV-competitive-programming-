class NumArray:

    def __init__(self, nums: List[int]):
        self.prefsum = [0]
        cur = 0
        for i in nums:
            cur += i
            self.prefsum.append(cur)
        
        

    def sumRange(self, left: int, right: int) -> int:
        
        rightSum = self.prefsum[right+1]
        leftSum = self.prefsum[left]
        
        return rightSum - leftSum
        
            
            
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)




