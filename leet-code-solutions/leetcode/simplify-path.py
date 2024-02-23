class Solution:
    def simplifyPath(self, path: str) -> str:
         x = []
         cur = ""
        #  x.append("/")
         for i in path + "/":
             if i == "/":
                 if cur == "..":
                     if x: x.pop()
                 
                 elif cur != "" and cur != "." :
                     x.append(cur)
                 
                 cur = ""
             else:
                 cur += i

         return "/" + "/" .join(x)
            


        