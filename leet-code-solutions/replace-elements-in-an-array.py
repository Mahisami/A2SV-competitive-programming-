class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = defaultdict(int)
        for id, val in enumerate(nums):
            d[val] = id
        

        for i in operations:
            nums[d[i[0]]] = i[1]
            d[i[1]] = d[i[0]]
           
        return nums