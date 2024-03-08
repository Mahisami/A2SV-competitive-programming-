class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start = [intervals[i][0] for i in range(len(intervals))]
        startt = sorted(start)

        ans = []
        for interval in intervals:
            res = bisect_left(startt, interval[1])
            ans.append(start.index(startt[res]) if res < len(intervals) else -1)
        return ans





        