class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        count = 0

        while l <= r:
            if nums[l] + nums[r] <= target:
                count += 2 ** (r - l)
                l += 1
            else:
                r -= 1

        return count % (10**9 + 7)