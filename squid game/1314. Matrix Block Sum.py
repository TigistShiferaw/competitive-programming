class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        prefix = [[0] * len(mat[0]) for i in range(len(mat))]
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if j == 0:
                    prefix[i][j] = mat[i][j]
                else:
                    prefix[i][j] = prefix[i][j - 1] + mat[i][j]
        
        
        ans = [[0] * len(mat[0])  for i in range(len(mat))]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                maxRow = min(len(mat) - 1, i + k)
                maxCol = min(len(mat[0]) - 1, j + k)
                minRow = max(0, i - k)
                minCol = max(0, j - k )
                temp = 0
                # print(minRow,maxRow,i,j,k, minCol)
                for m in range(minRow, maxRow + 1):
                    temp += prefix[m][maxCol]
                if minCol - 1 >= 0:
                    for m in range(minRow,maxRow + 1):
                        temp -= prefix[m][minCol - 1]
                ans[i][j] = temp
        return ans
