class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        print(target)
        n = len(s2)
        start = 0
        end = len(s1) - 1 


        while start < n and end < n:
            if Counter(s2[start:end+1]) == target:
                return True
            else:
                start += 1
                end += 1
        return False








            

        