class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        l = 0
        r = 0
        cnt = 0
        g.sort()
        s.sort()
        while r <= len(s)-1 and l <= len(g)-1:
            if s[r] >= g[l]:
                cnt += 1
                l += 1
            r += 1
        return cnt
        