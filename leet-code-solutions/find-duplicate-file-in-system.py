class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ans = []
        d = {}

        for i in paths:
            values = i.split(" ")
            # print(values)
            for j in range(1, len(values)):
                # print(values[j])
                start, end = values[j].split("(")
                content = end[:-1]  
        
                if content not in d:
                    d[content] = [values[0] + "/" + start]
                   
                else:
                    d[content].append(values[0] + "/" + start)
        

        for value in d.values():
            if len(value) > 1:
                ans.append(value)
                print(ans)

        return ans