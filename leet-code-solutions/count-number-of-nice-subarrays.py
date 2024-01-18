class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        out = 0
        cnt = 0
        e = 0
        l = 0
        n = len(nums)
        odd = 0  

        while e < len(nums):
            if nums[e] % 2 != 0:
                odd += 1
                cnt = 0

            while odd == k:
                cnt += 1
                odd -= nums[l] & 1
                
                l += 1

            out += cnt
            e += 1

        return out
