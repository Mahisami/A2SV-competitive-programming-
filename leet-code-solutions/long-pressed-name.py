class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

   
        l = 0
        r = 0

        while r < len(typed):
            if l < len(name) and name[l] == typed[r]:
                l += 1
                r += 1
            elif r == 0 or typed[r] != typed[r - 1]:
                return False
            else:
                r += 1

        return l == len(name)
