class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        output = ""
        spaces.append(len(s)+1)
        for i in range(0,len(s)):
            if spaces[0] == i:
                output += " "
                output += s[i]
                spaces.pop(0)
            else:
                output += s[i]
        return output

