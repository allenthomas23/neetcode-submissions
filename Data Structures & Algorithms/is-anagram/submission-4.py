class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        for l in s:
            if l in map1:
                map1[l] = map1[l] + 1
            else:
                map1[l] = 1
        for g in t:
            if g in map2:
                map2[g] = map2[g] + 1
            else:
                map2[g] = 1
        return map1==map2