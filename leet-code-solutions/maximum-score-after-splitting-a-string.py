class Solution:
    def maxScore(self, s: str) -> int:
        cnt1 = s.count("1")
        out = 0
        cnt0 = 0

        for i in range(len(s)-1):
            if s[i] == "1":
                cnt1 -= 1
            else:
                cnt0 += 1
            out = max(out, cnt0 + cnt1)
        return out