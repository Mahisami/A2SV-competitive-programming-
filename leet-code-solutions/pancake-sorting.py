class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = []

        for i in range(n, 1, -1):
         
            index = arr.index(i)
         
            arr[:index+1] = list(reversed(arr[:index+1]))
            ans.append(index+1)
           
            arr[:i] = list(reversed(arr[:i]))
            ans.append(i)

        return ans