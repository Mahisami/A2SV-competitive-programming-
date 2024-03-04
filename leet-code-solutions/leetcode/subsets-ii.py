class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sub = []
        s = []
        nums.sort()
        def back(i):
            if len(nums) <= i:

                ans.append(sub[:])
                return
            sub.append(nums[i])
            back(i+1)
            sub.pop()
            back(i+1)
        back(0)
        for i in range(len(ans)):
            if ans[i] not in s:
                s.append(ans[i])
            else:
                continue
        return s

        