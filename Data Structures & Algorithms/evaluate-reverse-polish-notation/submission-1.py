class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for a in tokens:
            if a == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif a == '-':
                stack.append(-1* int(stack.pop()) + int(stack.pop()))
            elif a == '*':
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif a == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(a))
        return stack[0]