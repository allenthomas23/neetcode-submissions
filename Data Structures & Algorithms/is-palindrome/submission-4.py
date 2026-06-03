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
            if newstr[i] != newstr[j]:
                valid = False
            j-=1
            i+=1
        return valid

        