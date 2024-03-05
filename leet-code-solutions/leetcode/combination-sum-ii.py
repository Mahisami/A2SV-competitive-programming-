class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        bucket = []
        ans = []
        candidates.sort()
        s = set()
        total = sum(candidates)
        visited = defaultdict(set)
        # @cache
        def backtrack(i,sum_, cur):
            bucket_tuple = tuple(sorted(bucket))
            if bucket_tuple in visited[i]:
                return
            visited[i].add(bucket_tuple)
            if sum_ == target:
                s.add(bucket_tuple)
                return
            if len(candidates) <= i:
                return
            # print(bucket,candidates[i])
            if sum_ > target or total - cur + sum_ < target:
                return
            if candidates[i] <= target:
                bucket.append(candidates[i])
                cur += candidates[i]
                sum_ += candidates[i]
                backtrack(i+1, sum_, cur)
                sum_ -= candidates[i]
                bucket.pop()
                backtrack(i+1, sum_, cur)

            
            # print(bucket,candidates[i])
            

        backtrack(0, 0, 0)
        for a in s:
            ans.append(list(a))

        return ans
        