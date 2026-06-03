class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strs:
            array = [0 for i in range(26)]
            for c in word:
                array[ord(c)-ord('a')] += 1
            hashmap[tuple(array)].append(word)
        return list(hashmap.values())
        


        