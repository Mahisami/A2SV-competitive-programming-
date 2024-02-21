class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        x = list(palindrome)
        if len(x) == 1:
            return ""
        if len(x) == x.count("a"):
            x[-1] = "b"
            return "".join(x)

        for i in range(len(x)):
            if x[i] != "a":
                if len(x) % 2 != 0:
                    if i == len(x) // 2:
                        x[-1] = chr(ord(x[i+1])+1)
                        return "".join(x)
                x[i] = "a"
                return "".join(x)

            else:
             
                if len(x) % 2 != 0:
                    if i == len(x) // 2:

                        x[i+1] = chr(ord(x[i+1])+1)
                        return "".join(x)


           
                    
            
               
         
    
        