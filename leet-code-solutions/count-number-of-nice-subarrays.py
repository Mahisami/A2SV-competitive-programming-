class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for num in range(len(nums)):
            if nums[num] % 2 != 0:
                nums[num] = 1
            else:
                nums[num] = 0
        
        d = {0:1}
        counter = 0
        pref = 0

        for number in nums:
            pref += number
            if pref - k in d:
                counter += d[pref - k]
            if pref in d:
                d[pref] += 1
            else:
                d[pref] = 1
        
        return counter