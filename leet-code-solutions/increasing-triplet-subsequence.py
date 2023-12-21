class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        maxA = float("inf")
        maxB = float("inf")

        for i in range(len(nums)):
            if nums[i] > maxB:
                return True
            elif nums[i] <= maxA:
                maxA = nums[i]
            else:
                maxB = nums[i]