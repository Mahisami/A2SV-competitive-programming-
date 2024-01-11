class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        cnt = 0
        max_len = 0
        start = 0

        for i in range(len(s)):
            if s[i] in vowels:
                cnt += 1

            if i >= k:
                if s[start] in vowels:
                    cnt -= 1
                start += 1

            max_len = max(max_len, cnt)

        return max_len
