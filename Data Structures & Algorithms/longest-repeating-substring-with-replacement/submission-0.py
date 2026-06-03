class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        hashmap = {}
        for r, c in enumerate(s):
            hashmap[c] =  1 + hashmap.get(c,0)
            while(r-l+1 - max(hashmap.values()) > k):
                hashmap[s[l]] -=1
                l+=1
            res = max(res, r-l+1)
        return res