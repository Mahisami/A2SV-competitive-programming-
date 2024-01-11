class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        max_len = 0
        count = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1

            if count > k:
                if nums[l] == 0:
                    count -= 1
                l += 1
            max_len = max(max_len, i - l + 1)
        return max_len
                    