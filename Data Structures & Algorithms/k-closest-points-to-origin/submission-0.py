import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists=[]
        heapq.heapify(dists)
        for point in points:
            x,y = point
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(dists,(dist,point))
        res = []
        for i in range(k):
            dp = heapq.heappop(dists)
            res.append(dp[1])
        return res