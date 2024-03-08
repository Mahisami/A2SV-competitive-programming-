class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        l = len(nums)
        ans = [-1]*l

        for i in range(l*2):
            val = i % l
            while stack and nums[stack[-1]] < nums[val]:
                ans[stack.pop()] = nums[val]
            stack.append(val)
        return ans
        