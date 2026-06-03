class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        for c in s:
            if c in map1:
                map1[c] = map1[c] +1
            else:
                map1[c] = 1
        for c in t:
            if c in map2:
                map2[c] = map2[c] +1
            else:
                map2[c] = 1
        return map1==map2
