class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = {}
        for i in matches:
           
            if i[1] not in d:
                d[i[1]]=1
            else:
                d[i[1]]+=1
        print(d)

        winner=[]
        losser=[]
        for i in matches:
            if d[i[1]]==1:
                losser.append(i[1])
            if i[0] not in d:
                winner.append(i[0])
                d[i[0]]=2
        print(d)
        winner.sort()
        losser.sort()
        return [winner,losser]



        