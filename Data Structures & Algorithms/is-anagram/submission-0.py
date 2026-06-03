class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = defaultdict()
        map2 = defaultdict()
        for letter in s:
            if letter in map1:
                map1[letter] = map1[letter] + 1
            else:
                map1[letter] = 1
        for letter in t:
            if letter in map2:
                map2[letter] = map2[letter] + 1
            else:
                map2[letter] = 1
        if map1==map2:
            return True
        return False