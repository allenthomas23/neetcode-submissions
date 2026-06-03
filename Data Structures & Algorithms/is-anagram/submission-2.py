class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table1 = {}
        table2 = {}
        for i in s:
            table1[i] = table1.get(i, 0) + 1
        for i in t:
            table2[i] = table2.get(i, 0) + 1
        return table1 == table2
