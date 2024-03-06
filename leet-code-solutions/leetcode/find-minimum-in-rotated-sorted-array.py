class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        
        while l < r:
            mid = (l+r)//2
            if nums[l] > nums[mid]:
                r = mid
                # if nums[l] < nums[mid]:
                #     return nums[l]
            elif nums[r] < nums[mid]:
                l =  mid+1
            else:
                return nums[l]
            
        return nums[l]
        