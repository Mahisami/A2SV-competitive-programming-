class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total = sum(nums)
        prefsum = 0
        out = []

        for i in range(n):
            suffsum = total - prefsum - nums[i] * (n - i)
            leftsum = nums[i] * i - prefsum
            out.append(leftsum + suffsum)
            prefsum += nums[i]

        return out
