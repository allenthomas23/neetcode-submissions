class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = set('+*/-')
        num1,num2 = 0,0
        res = 0
        for i in range(len(tokens)):
            if tokens[i] in op:
                num1 = stack.pop()
                num2 = stack.pop()
                if tokens[i] == '-':
                    res = num2 - num1
                elif tokens[i] == '+':
                    res = num1 + num2
                elif tokens[i] == '*':
                    res = num1 * num2
                elif tokens[i] == '/': 
                    res = int(num2/num1)
                stack.append(res)
            else:
                stack.append(int(tokens[i]))
        return stack[0]
        