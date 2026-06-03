class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        count = {}
        for n in nums:
            count[n] = 1+count.get(n,0)
        sort = list(sorted(count.items(), key=lambda item: item[1], reverse=True))
        res = sort[:k]
        real = []
        for l in res:
            real.append(l[0])
        return real
