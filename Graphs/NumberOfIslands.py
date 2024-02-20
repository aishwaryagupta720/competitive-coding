class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        def dfs(x,y):
            if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]) or grid[x][y]=="0":
                return
            grid[x][y]="0"
            dfs(x,y+1)
            dfs(x,y-1)
            dfs(x+1,y)
            dfs(x-1,y)


        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]=="1":
                    count+=1
                    dfs(x,y)
        return count
        
        

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1