class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        n = len(distance)
        total = sum(distance)
        if start > destination:
            start, destination = destination, start
        clockwise = sum(distance[start:destination])
        anticlock = total - clockwise
        return min(clockwise, anticlock)
       

        