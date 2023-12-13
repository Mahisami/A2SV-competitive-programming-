class Solution:
    def minimizedStringLength(self, s: str) -> int:
        ss = set()
        for i in range(len(s)):
            ss.add(s[i])
        return len(ss)
        