class Solution:
    def minimumSteps(self, s):
        shift = 0
        step = 0
        for i in range(len(s)):
            if s[i] == "0":
                step += i - shift
                shift += 1
        return step