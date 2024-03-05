class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        bucket = []
        def back(i):
            if len(bucket) == k:
                ans.append(bucket.copy())
                return 
            if i > n:
                return 
            bucket.append(i)
            back(i+1)
            bucket.pop()
            back(i+1)

        back(1) 
        return ans

            
            
                    