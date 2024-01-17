
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        start = 0
        end = 0
        d = defaultdict(int)

        max_beauty = 0

        while end < len(s):
            d[s[end]] += 1

            while (end - start + 1) - max(d.values()) > k:
                d[s[start]] -= 1
                start += 1

            max_beauty = max(max_beauty, end - start + 1)

            end += 1

        return max_beauty
