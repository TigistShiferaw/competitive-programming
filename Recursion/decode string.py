class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        ans=""
        x=0
        for i in s:
            st=""
            num=""
            if i!="]":
                stack.append(i)
            elif i=="]":
                while stack[-1]!="[" and stack:
                    st+=stack.pop()
                    
                if stack: 
                    stack.pop() 
                    
                    while stack and (stack[-1]=="0"or stack[-1]== "1"or stack[-1]=="2"or stack[-1]=="3"or stack[-1]=="4" or stack[-1]=="5"or stack[-1]=="6" or stack[-1]=="7"or stack[-1]== "8"or stack[-1] =="9"):
                        if stack:
                            num+=stack.pop()
                    num=num[::-1]    
                    x=int(num)
                 
                for j in range(x):
                    for n in range(len(st)-1,-1,-1):
                         stack.append(st[n])           
        for i in range(len(stack)):
            ans+=stack[i]
        return ans    
                
                