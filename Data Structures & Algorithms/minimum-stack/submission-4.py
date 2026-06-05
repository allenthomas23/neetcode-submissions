class MinStack:

    def __init__(self):
        self.stack = []
        self.minnum = float('infinity')
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minnum = min(val,self.minnum)
        self.minstack.append(self.minnum)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        if self.stack:
            self.minnum = self.minstack[-1]
        else:
            self.minnum = float('infinity')
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        
        return self.minnum
