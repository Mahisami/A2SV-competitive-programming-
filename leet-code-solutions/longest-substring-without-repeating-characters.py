class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:  
        d = defaultdict(lambda : 0)   
        max_len = 0
        start = 0
        for i in range(len(s)):
            d[s[i]] += 1
            while d[s[i]] > 1:
                d[s[start]] -= 1
                start += 1
            max_len = max(max_len,i-start+1)
        return max_len
            
                



                
            

            

            