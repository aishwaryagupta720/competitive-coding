class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        queue=[]
        maxd=0
        vector=[[1,0],[-1,0],[0,1],[0,-1]]
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]==1:
                    queue.append([x,y])
        # if all water or all land
        if len(queue)==0 or len(queue)==len(grid)*len(grid[0]):
            return -1
        
        while len(queue)>0:
            prevx,prevy=queue.pop(0)
            for op in vector:
                x=prevx+op[0]
                y=prevy+op[1]
                if (x<0 or y<0 
                    or x>len(grid)-1 or y>len(grid[0])-1
                    or grid[x][y]!=0):
                    continue
                else:
                    grid[x][y]=grid[prevx][prevy]+1
                    queue.append([x,y])
                    maxd=max(maxd,grid[x][y])
        # because we started with 1 instead of 0 
        return maxd-1


        
# Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

# The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

 

# Example 1:


# Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
# Output: 2
# Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
# Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

# The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.


