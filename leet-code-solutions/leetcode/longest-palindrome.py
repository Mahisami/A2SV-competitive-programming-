class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        total = 0
        flag = True

        for key, val in cnt.items():
            
            if val % 2 == 0:
                total += val
            else:
                flag = False
                val -= 1
                total += val 
        if flag:
            return total
        else:
            return total+1

        