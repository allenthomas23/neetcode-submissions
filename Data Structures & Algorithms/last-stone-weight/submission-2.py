class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *=-1
        
        heap = stones
        heapq.heapify(heap)
        while len(heap) > 1:
            x = heapq.heappop(heap) * -1
            y = heapq.heappop(heap) * -1
            if x>y:
                new = x-y
                heapq.heappush(heap,-new)
        
        return heap[0] * -1 if heap else  0

