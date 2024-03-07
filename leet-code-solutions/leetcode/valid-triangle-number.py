class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                summo = nums[i] + nums[j]
                val = bisect_left(nums, summo)
                ans += max(0, val - j - 1)
        return ans
                        

        