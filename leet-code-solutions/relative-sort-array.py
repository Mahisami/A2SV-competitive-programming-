class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr = []
        not_in_arr = []
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr2[i] == arr1[j]:
                    arr.append(arr1[j])
        not_in_arr = [x for x in arr1 if x not in arr2]

        not_in_arr.sort()
        arr.extend(not_in_arr)
        return arr

           


        