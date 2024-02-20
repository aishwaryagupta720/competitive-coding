class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area=0
        sum=0
        def dfs(x,y):
            nonlocal area,sum
            if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]) or grid[x][y]==0:
                return
            sum+=1
            area=max(area,sum)
            grid[x][y]=0
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)
            
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]==1:
                    sum=0
                    dfs(x,y)
        return area
        
# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.