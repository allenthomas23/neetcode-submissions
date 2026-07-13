class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        chars = set(tasks)
        count = []
        for char in chars:
            count.append(-(tasks.count(char)))
        heapq.heapify(count)
        queue = deque()
        time = 0
        while(count or queue):
            time+=1
            if count:
                cnt = heapq.heappop(count) * -1 - 1
                if cnt:
                    queue.append([cnt,time+n])
            if queue and queue[0][1]<=time:
                heapq.heappush(count,queue.popleft()[0] * -1)
        return time