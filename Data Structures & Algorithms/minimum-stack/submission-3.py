class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            min_top = val
        else:
            min_top = min(self.stack[-1][1], val)
        self.stack.append([val, min_top])

    def pop(self) -> None:
        return self.stack.pop()[0]      

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
