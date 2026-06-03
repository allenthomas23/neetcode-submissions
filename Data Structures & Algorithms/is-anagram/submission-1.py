class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table1 = {}
        table2 = {}
        for i in s:
            if i in table1:
                table1[i] = table1.get(i) + 1
            else:
                table1[i] = 1
        for i in t:
            if i in table2:
                table2[i] = table2.get(i) + 1
            else:
                table2[i] = 1
        return table1 == table2
