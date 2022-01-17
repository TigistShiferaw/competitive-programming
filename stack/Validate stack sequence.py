class Solution:
    
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        arr=[]
        x=len(popped)-1
        p1=0
        for i in range(len(pushed)):
            stack.append(pushed[i])  
            while stack and stack[-1]==popped[p1]:
                    stack.pop()
                    p1+=1 
                    
        while stack and popped[p1]==stack[-1] and p1<len(popped):
                stack.pop()
                p1+=1
        if len(stack)==0:
             return True
        else:
             return False
                         
            
     
                
        