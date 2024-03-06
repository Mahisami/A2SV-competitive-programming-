class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        x = bisect_right(nums, target)
        y = bisect_left(nums, target)
        out= []
        out.append(y)
        out.append(x-1)
        return out
        # print([y,x-1])
        