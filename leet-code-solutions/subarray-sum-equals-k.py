class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count  = 0
        prefsum = 0
        d = defaultdict(int)
        d[0] = 1
        for i in range(len(nums)):
            prefsum += nums[i]
            if prefsum - k in d:
                count += d[prefsum - k]
            d[prefsum] += 1
        return count

        
        
        