

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        l, r = 0, 1
        flag = False

        while r < len(arr) and arr[l] < arr[r]:
            flag = True
            r += 1
            l += 1

        if l == 0 or r == len(arr):
            return False

        while r < len(arr) and arr[l] > arr[r]:
            flag = True
            r += 1
            l += 1

        return flag and r == len(arr)
