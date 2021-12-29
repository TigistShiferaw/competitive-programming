class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        st=""
        solution=""
        for i in range(len(s)):
            if s[i]!=')':
                stack.append(s[i])
            else:
                st=""
                while stack[-1]!='(':
                    st+=stack.pop()
                stack.pop()    
                for j in range(len(st)):
                    stack.append(st[j])
        for i in range(len(stack)):
            solution+=stack[i]
        return solution
                    
               
            
                
            