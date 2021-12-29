class MyCircularDeque:

    def __init__(self, k: int):
        self.queue=[]
        self.k=k
    def insertFront(self, value: int) -> bool:
        
        if self.isFull()==True:
            return False
        else :
            self.queue.insert(0,value)
        return True

    def insertLast(self, value: int) -> bool:
        
        if self.isFull()==True:
            return False
        else:
            self.queue.append(value)
        return True

    def deleteFront(self) -> bool:
        size=len(self.queue)
        if size>0:
            self.queue.pop(0)
            return True
        return False

    def deleteLast(self) -> bool:
        size=len(self.queue)
        if size >0 :
            self.queue.pop()
            return True
        
        return False

    def getFront(self) -> int:
        if self.isEmpty()==False:
            return self.queue[0]
        return -1
    def getRear(self) -> int:
        if self.isEmpty()==False:
            return self.queue[-1]
        return -1 
    def isEmpty(self) -> bool:
        if len(self.queue)==0:
            return True
        return False

    def isFull(self) -> bool:
        if len(self.queue)==self.k:
            return True
        return False

