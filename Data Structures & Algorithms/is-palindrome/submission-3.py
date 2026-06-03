class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""
        i =0
        valid = True
        for c in s:
            if c.isalnum():
                newstr += c.lower()
        j = len(newstr)-1

        while i < j:
            while not newstr[i].isalnum():
                i +=1
            while not newstr[j].isalnum():
                j-=1
            if newstr[i] != newstr[j]:
                valid = False
            j-=1
            i+=1
        return valid

        