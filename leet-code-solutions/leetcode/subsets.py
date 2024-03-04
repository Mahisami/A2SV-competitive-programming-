class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = []
        sub = []

        def backtrack(i):
            if len(nums) <= i:
                arr.append(sub[:])
                return
            sub.append(nums[i])
            backtrack(i+1)
            sub.pop()
            backtrack(i+1)
            

        backtrack(0)
        return arr
        