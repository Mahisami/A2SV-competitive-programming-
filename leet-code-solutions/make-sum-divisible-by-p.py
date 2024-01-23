class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target_rem = total % p

        if target_rem == 0:
            return 0
        
        cur_sum = 0
        d = {0:-1}
        cur_rem= 0
        min_val = len(nums)

        for i, num in enumerate(nums):
            cur_sum += num
            cur_rem = cur_sum % p
            rem = (cur_rem - target_rem + p) % p

            if rem in d:
                min_val = min(min_val, i - d[rem])
            d[cur_rem] = i

        return min_val if min_val < len(nums) else -1

