class MyQueue:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        
    def push(self, x: int) -> None:
        self.stack1.append(x)
    def pop(self) -> int:
        if len(self.stack2)==0:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
    def peek(self) -> int:
        if len(self.stack2)==0:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
    def empty(self) -> bool:
        if len(self.stack1)==0 and len(self.stack2)==0:
            return True
        return False
