class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        st=""
        arr=[]
        for i in s:
            if i!='*' and i!='/' and i!='-' and  i!='+':
                st+=i
            elif i=='*' or i== '/' or  i=='-' or i== '+':
                arr.append(st)
                arr.append(i) 
                st=""
        arr.append(st) 
        i=0
        while i in range(len(arr)):
            if arr[i]!='*' and arr[i]!='/':
                if arr[i]=='+' or arr[i]=='-':
                    stack.append(arr[i])
                    i+=1
                else:
                    stack.append(int(arr[i]))
                    i+=1
                        
            elif  arr[i]=='*':
                i=i+2
                x=stack.pop()
                y=int(arr[i-1])
                stack.append(x*y)
            elif arr[i]=='/':
                i=i+2
                x=stack.pop()
                y=int(arr[i-1])
                stack.append(x//y)
        stack2=[] 
        ans=0
        stack=stack[::-1]
    
        while stack:
            if stack[-1]!='-' and stack[-1] != '+':
                ans+=int(stack.pop())
            elif stack[-1]=='-':
                stack.pop()
                ans-=int(stack.pop())
            elif stack[-1]=='+':
                stack.pop()
                ans+=int(stack.pop())
            
        return ans 
        
                    