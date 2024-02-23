class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        y = collections.deque()

        for i in range(len(nums)):
            while y and nums[y[-1]] < nums[i]:
                y.pop()
            y.append(i)
            if i - y[0] >= k:
                y.popleft()

            if i + 1 >= k:
                ans.append(nums[y[0]])

        return ans
