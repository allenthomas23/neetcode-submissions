class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for i in s:
            if i.isalnum():
                string += i.lower()

        j = len(string)-1
        for i in range(len(string)//2):
            if string[i] != string[j-i]:
                return False
        return True

