class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        hashmap = {"}" : "{", ")":"(", "]": "["}
        for c in s:
            if c in hashmap.values():
                stack.append(c)
            else:
                # if (true if stack empty) or top doesnt match correct pair
                if not stack or stack.pop() != hashmap.get(c):
                    return False
        return not stack
