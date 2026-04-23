class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        del self.stack[-1]
        
    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        aux = self.stack[0]        
        for item in self.stack:
            if aux > item:
                aux = item       
        return aux 
        
