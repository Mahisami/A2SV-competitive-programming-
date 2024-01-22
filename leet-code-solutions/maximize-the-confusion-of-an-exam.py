class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        out = 0
        l = 0
        r = 0
        max_len = 0
        d = defaultdict(int)
        for i in range(len(answerKey)):
            d[answerKey[i]] += 1

            if min(d["T"],d["F"]) > k:
                
                d[answerKey[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len

                
        

