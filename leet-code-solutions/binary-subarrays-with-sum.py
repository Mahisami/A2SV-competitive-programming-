class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pref = 0
        out = 0
        cnt = Counter()
        cnt[0] = 1
        for num in nums:
            pref += num
            out += cnt[pref-goal]
            cnt[pref] += 1
      
        return out