class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posrequired=[]
        timerequired=[]
        spe=[]
        dic={}
        stack=[]
        for i in range(len(position)):
            dic[position[i]]=speed[i]
        position.sort(reverse=True)
        for i in position:
            spe.append(dic[i])
        for i in range (len(position)):
            posrequired.append(target-position[i])
        for i in range(len(position)):
            timerequired.append(posrequired[i]/spe[i])
        i=0
        stack.append(timerequired[0])
        while stack and i<len(timerequired):
            if timerequired[i]>stack[-1]:
                stack.append(timerequired[i])
            i+=1
        
        return len(stack)
        