class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        arr = self.getRow(rowIndex - 1)
        
        newarr = [0 for k in range(rowIndex+1)]
        
        newarr[0] = 1
        newarr[-1] = 1
        for j in range(1, len(newarr)-1):
            newarr[j] = arr[j] + arr[j-1]
        return newarr
  

      
 
