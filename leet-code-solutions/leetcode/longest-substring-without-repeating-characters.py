class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = 0
        length = 0
        for i in range(len(s)):  
            while s[i] in window:
                window.remove(s[l])
                l += 1
            
            length = max(length, i - l + 1)
            window.add(s[i])
        return length

            

            