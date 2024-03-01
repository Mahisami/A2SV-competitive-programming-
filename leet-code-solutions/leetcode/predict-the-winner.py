class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def ans(i,j):
            if i == j:
                return nums[i]
            return max((nums[i] - ans(i + 1, j)), (nums[j] - ans(i, j - 1)))
        if ans(0,len(nums)-1) < 0:
            return False
        return True

        