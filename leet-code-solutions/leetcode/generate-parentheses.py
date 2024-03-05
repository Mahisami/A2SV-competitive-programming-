class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        bucket = []
        ans = []
        
        def back(cur,o, c):
            if len(cur) == 2*n:
                ans.append("".join(cur))
                return
            if o < n:
                back(cur + "(",o+1,c)
                # cur += "("
            if c < o:
                back(cur+")",o,c+1)
                # cur += ")"
            
        back("",0,0)
        return ans


        