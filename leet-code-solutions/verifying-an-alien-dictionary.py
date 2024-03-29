class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
       
        d = {}
        for index, val in enumerate(order):
            d[val] = index

        for i in range(len(words) - 1):

            for j in range(len(words[i])):
                if j >= len(words[i + 1]): return False

                if words[i][j] != words[i + 1][j]:
                    if d[words[i][j]] > d[words[i + 1][j]]: return False

                    break

        return True
        

        