class MinStack:

    def __init__(self):
        self.stack=[]
        
    def push(self, val: int) -> None:
        temp = self.getMin()
        
        if temp==None or temp>val  :
            temp=val
        self.stack.append((val,temp))
        
    def pop(self) -> None:
        
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack)==0:
            return None
        return self.stack[-1][1]
