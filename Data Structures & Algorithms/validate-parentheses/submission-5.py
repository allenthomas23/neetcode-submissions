class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        hashmap = {"}" : "{", ")":"(", "]": "["}
        if len(s) == 1:
            return False
        for i,c in enumerate(s):
            if c in hashmap.values():
                stack.append(c)
            else:
                # if opening == hasmap.
                if not stack or stack.pop() != hashmap.get(c):
                    return False
        return not stack
