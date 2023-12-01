class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0
        i = 0
        result = 0
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        while i < len(s):
            output = d[s[i]]
            if (i+1) < len(s) and d[s[i]] < d[s[i+1]]:
                output = d[s[i+1]] - d[s[i]]
                i += 1
            i+=1
            result += output
           

        return result

    
    