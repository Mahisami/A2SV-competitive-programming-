class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        summ = 0
        for i in nums:
            summ += i

            if summ > max_sum:
                max_sum = summ
            if summ < 0:
                summ = 0
        return max_sum
        