class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        output = []
        
        for c in range(len(matrix[0])):
            arr = []
            for r in range(len(matrix)):
                arr.append(matrix[r][c])
            output.append(arr)
            
        return output
            