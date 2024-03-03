class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        m = len(set(nums))
        cnt = 0

        for i in range(n):
            s = set()
            for j in range(i, n):
                s.add(nums[j])

                if m == len(s):
                    cnt += 1
        return cnt
                            