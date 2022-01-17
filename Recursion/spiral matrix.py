class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        arr=[]
        def order(matrix):
            if not matrix:
                return 
            else:
                x=matrix.pop(0)
                for i in x:
                    arr.append(i)
                if matrix:    
                    for i in range(len(matrix)):
                        if matrix[i]:
                            y=matrix[i]
                            z=y.pop()
                            arr.append(z)  
                if matrix:    
                    c=matrix[-1]    
                    m=len(c)    
                    for i in range(m-1,-1,-1):
                        y=matrix[-1]
                        arr.append(matrix[-1][i])
                        if y:
                            z=y.pop() 
                if matrix:       
                    m=len(matrix)    
                    for i in range(m-1,-1,-1):
                        if matrix[i]:
                            arr.append(matrix[i][0])
                            matrix[i].pop(0)
                if matrix  :          
                    matrix.pop()                        
                order(matrix) 
            
        order(matrix) 
        return arr