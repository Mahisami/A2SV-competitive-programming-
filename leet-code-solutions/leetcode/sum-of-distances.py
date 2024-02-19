class Solution:
    def distance(self, nums: List[int]) -> List[int]:     
        d = defaultdict(list)
        n = len(nums)
        for i, v in enumerate(nums):
            d[v].append(i)
        li = [0]*n
        
        for key,val in d.items():
            pre = 0
            suf = sum(val)
            n,m = 0, len(val)
            
            for i in val:
                pre += i
                suf -= i
                
                n += 1
                m -= 1
                
                li[i] = -pre + i*n + suf - i*m
        return li
                