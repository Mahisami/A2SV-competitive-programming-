class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        x = points.sort(key = lambda x: x[1])
        cnt = 1
        curr = points[0][1]
        for i in range(1,len(points)):
            
            print(cnt)

            if curr < points[i][0]:
                cnt += 1
                curr = points[i][1]
            else:
                continue
        return cnt



        