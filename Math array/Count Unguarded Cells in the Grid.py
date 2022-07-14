class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [[0]* n  for _ in range(m)]
        
        for x,y in guards:
            matrix [x][y] = 1
        for x,y in walls:
            matrix[x][y] = 2
        for i in range(m):
            c = 0
            for j in range(n):
                if matrix[i][j] == 1:
                    c = 3
                elif matrix[i][j] == 2:
                    c = 0
                elif matrix[i][j] == 0:
                    if c == 3:
                        matrix[i][j] = 3
        for i in range(m):
            c = 0
            for j in range(n - 1,-1,-1):
                if matrix[i][j] == 1:
                    c = 3
                elif matrix[i][j] == 2:
                    c = 0
                elif matrix[i][j] == 0:
                    if c == 3:
                        matrix[i][j] = 3
        for j in range(n):
            c =0 
            for i in range(m):
                if matrix[i][j] == 1:
                    c = 3
                elif matrix[i][j] == 2:
                    c = 0
                elif matrix[i][j] == 0:
                    if c == 3:
                        matrix[i][j] = 3
                
        for j in range(n):
            c = 0
            for i in range(m - 1, -1, -1):
                
                if matrix[i][j] == 1:
                    c = 3
                elif matrix[i][j] == 2:
                    c = 0
                elif matrix[i][j] == 0:
                    if c == 3:
                        matrix[i][j] = 3
        count = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    count += 1
        return count
            
                        
                
            
            
    