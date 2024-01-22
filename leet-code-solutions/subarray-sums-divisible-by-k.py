class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cnt = 0
        d = defaultdict(int)
        d[0] = 1
        pref = 0

        for i in range(len(nums)):
            pref += nums[i]

            mod = pref % k
            if mod < 0:
                mod += k
            cnt += d[mod]
            d[mod] += 1
        return cnt
                


        