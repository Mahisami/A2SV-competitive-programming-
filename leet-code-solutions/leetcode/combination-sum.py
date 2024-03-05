class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        N = len(candidates)
        path = []

        def helper(i, cur_sum):
            if cur_sum == target:
                ans.append(path[:])
                return
            if i == N:
                return
            if cur_sum > target:
                return
            max_add = (target - cur_sum)//candidates[i]

            helper(i + 1, cur_sum)
            for _ in range(max_add):
                path.append(candidates[i])
                cur_sum += candidates[i]
                helper(i + 1, cur_sum)
            for _ in range(max_add):
                path.pop()

        helper(0, 0)
        return ans