class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators=["+","-","/","*"]
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(tokens[i])
            else:
                x=int(stack.pop())
                y=int(stack.pop())
                if tokens[i]=="+":
                    stack.append(y+x)
                elif tokens[i]=="-":
                    stack.append(y-x)
                elif tokens[i]=="*":
                    stack.append(y*x)
                else:
                    stack.append(int(y/x))
        return stack.pop()
        