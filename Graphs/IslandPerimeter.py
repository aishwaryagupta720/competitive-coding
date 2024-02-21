class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter=0
        def dfs(x,y):
            nonlocal perimeter
            if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]) or grid[x][y]==0:
                return 1
            if grid[x][y]==-1:
                return 0
            grid[x][y]=-1
            count=0
            count+=dfs(x,y+1)
            count+=dfs(x,y-1)
            count+=dfs(x+1,y)
            count+=dfs(x-1,y)
            perimeter+=count
            return 0
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]==1:
                    dfs(x,y)
                    break
            if grid[x][y]==-1:
                break
        
        return perimeter
        

# 463. Island Perimeter

# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.