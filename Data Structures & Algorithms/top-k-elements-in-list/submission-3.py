from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        countValues = defaultdict(list)
        for num, freq in  count.items():
            countValues[freq].append(num)

        res = []

        for freq in range(len(nums),0,-1):
            for num in countValues[freq]:
                res.append(num)
                if len(res) ==k:
                    return res
            


        