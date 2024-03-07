class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        r = max(nums)
        ans = 0

        while l <= r:
            mid = l + (r - l)//2

            summ = 0
            for i in nums:
                summ += math.ceil(i/mid)
            if summ <= threshold:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
            
        