class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        output = []
        d = defaultdict(list)
        
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                # print(mat[r][c])
                key = r+c
                d[key].append(mat[r][c])
            # print(d[key])
            
        for key, values in d.items():
            if key % 2 == 0:
                
                d[key].reverse()
            output.extend(d[key])
        return output
        
                
                
        
        
        
        
        
        