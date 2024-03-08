class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        curMax = 0
        patches = 0

        for num in nums:
            if num > n:
                break

            while curMax < num - 1:
                curMax += curMax + 1
                patches += 1

            curMax += num

        while curMax < n:
            curMax += curMax + 1
            patches += 1

        return patches
