class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = set()

        for r in ranges:
            for num in range(r[0], r[1] + 1):
                covered.add(num)

        for num in range(left, right + 1):
         
            if num not in covered:
                return False

        return True
            
           

        