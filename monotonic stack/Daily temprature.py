class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]: 
        result=[0]*len(temperatures)
        stack=[]
    
        for i in range(len(temperatures)):
            while stack and temperatures[i]>stack[-1][0]:
                x,index=stack.pop()
                result[index]=(i-index)
            stack.append([temperatures[i],i])  
        return result 