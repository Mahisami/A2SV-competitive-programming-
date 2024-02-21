class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans ={}
        for i , x in enumerate(s):
            ans[x] = i
        print(ans)
        val = []
        si = e = 0
        for i, x in enumerate(s):
            si += 1
            e = max(e,ans[x])

            if i == e:
                val.append(si)
                si = 0
        return val




        