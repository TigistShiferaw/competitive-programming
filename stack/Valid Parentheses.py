class Solution:
    def isValid(self, s: str) -> bool:
        openingstringTypes="({["
        stack=[]
        for i in s:
            if i in openingstringTypes:
                stack.append(i)
            else:
                if len(stack)==0:
                    return False    
                compare=stack.pop()
                if compare=='{' and i!='}':
                    return False
                elif compare=='[' and  i!= ']':
                    return False
               
                elif compare=='(' and i!=')':
                     return False
        if len(stack)!=0:
            return False         
    
        return True