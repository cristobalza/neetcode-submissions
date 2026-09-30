class MinStack:

    def __init__(self):
        self.max_stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.max_stack.append(val)

        min_val = min(val, self.min_stack[-1] if self.min_stack else val)

        self.min_stack.append(min_val)
        

    def pop(self) -> None:

        self.max_stack.pop()
        self.min_stack.pop()

        

    def top(self) -> int:
        return self.max_stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
