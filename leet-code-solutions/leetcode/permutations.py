class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        bucket = []

        def back():
            if len(nums) == len(bucket):
                ans.append(bucket.copy())
                return
           
            for j in range(len(nums)):
                if nums[j] in bucket:
                    continue
                bucket.append(nums[j])
                back()
                bucket.pop()

        back()
        return ans