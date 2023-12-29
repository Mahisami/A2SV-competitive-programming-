class Solution:
    
    def sortSentence(self, s: str) -> str:
        ss = s[::-1].split()
        s1 = sorted(ss)
        print(s1)
        lst = []
        for i in s1:
            lst.append(i[1::][::-1])
    
        return (" ".join(lst))

                
        

                
        