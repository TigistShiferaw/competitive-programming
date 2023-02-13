class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        Dir = [(0,1), (1,0),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
        
        def isBound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid)

        heap = []
        if grid[0][0] == 0:
            heapq.heappush(heap,(1,0,0))
        vis = set()
        # print(isBound(2,2))
        while heap:
            # print(heap, vis)
            dist , x, y = heappop(heap)
            if (x, y) == (len(grid) - 1, len(grid) - 1):
                return dist 
            for D in Dir:
                new_row = x + D[0]
                new_col = y + D[1]
                new_dist = dist + 1
                
                if isBound(new_row, new_col) and grid[new_row][new_col] == 0 and (new_row, new_col) not in vis:
                    heappush(heap, (new_dist, new_row, new_col))
                    # print(new_row, new_col)
                    vis.add((new_row, new_col))
        return -1
            
