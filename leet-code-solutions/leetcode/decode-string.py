class Solution:
    def decodeString(self, s: str) -> str:
        
        def decoded(s):
            res = []
            n = len(s)
            i = 0
            

            while i < n:
                num = ""
                
                if s[i] in "0123456789":
                    ch = ""
                    

                    while s[i] in "0123456789":
                        num += s[i]
                        i += 1
                        
                    num = int(num)

                    p = 1
                    i += 1

                    while p != 0:
                        
                        if s[i] == "[":
                            p += 1
                            ch += "["
                        elif s[i] == "]":
                            p -= 1
                            if p != 0:
                                ch += "]"
                        else:
                            ch += s[i]
                        i += 1
                    res.append(decoded(ch) * num)
                else:
                    res.append(s[i])
                    i += 1
            return "".join(res)
        res = decoded(s)
        return res



        
        
                
                        
        

                



        