class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        last = "N"
        currPoint = (0,0)
        for index in range(len(instructions)):
            if last == "N":
                if instructions[index] == "G":
                    currPoint = (currPoint[0], currPoint[1] + 1)
                    
                elif instructions[index] == "L":
                    last = "W"
                    
                elif instructions[index] == "R":
                    last = "E"
                    
            elif last == "S":
                if instructions[index] == "G":
                    currPoint = (currPoint[0], currPoint[1] - 1)
                    
                elif instructions[index] == "L":
                    last = "E"

                elif instructions[index] == "R":
                    last = "W"
                    
            elif last == "W":
                if instructions[index] == "G":
                    currPoint = (currPoint[0] - 1, currPoint[1])
                    
                    
                elif instructions[index] == "L":
                    
                    last = "S"
                    
                elif instructions[index] == "R":
                    last = "N"
                    
            elif last == "E":
                if instructions[index] == "G":
                    currPoint = (currPoint[0] + 1, currPoint[1])
                    
                elif instructions[index] == "L":
                    last = "N"
                    
                elif instructions[index] == "R":
                    last = "S"
                    
           
        if currPoint == (0,0) or last != "N":
            return True
        return False