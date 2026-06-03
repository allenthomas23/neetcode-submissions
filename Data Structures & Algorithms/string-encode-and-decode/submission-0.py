class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            string = str(len(string))+'#' + string
            res+=string
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        while i <  len(s):
            j=i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j+1+length
        return res