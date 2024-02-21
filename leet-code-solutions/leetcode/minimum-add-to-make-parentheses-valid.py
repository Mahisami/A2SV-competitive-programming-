class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        cnt = 0
        out = []
        # if out == "":
        #     return 1
        if out == []:
            out.append(s[0])
        
        for i in range(1,len(s)):
            # print(out[-1])
            if out == []:
                out.append(s[i]) 
            elif out[-1] == "(" and s[i] == ")":
                del(out[-1])
            else:
                out.append(s[i])
        return len(out)



        # if s == "":
        #     cnt += 1

        # for i in range(len(s)):
            
        #     if s[i] == "(" and s[i+1] == ")":
        #         if 
        