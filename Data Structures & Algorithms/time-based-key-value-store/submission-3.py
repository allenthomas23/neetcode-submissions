class TimeMap:

    def __init__(self):
        self.hmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hmap:
            self.hmap[key] = []
        self.hmap[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmap:
            return ""
        pairs = self.hmap[key]
        l =0
        r = len(pairs)-1
        res = ""
        while(l<=r):
            m = (l+r)//2
            if pairs[m][1] > timestamp:
                r = m -1
            elif pairs[m][1] < timestamp:
                res= pairs[m][0]
                l = m +1
            else:
                return pairs[m][0]
        return res

        
        
