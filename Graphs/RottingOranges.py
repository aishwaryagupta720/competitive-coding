class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue=[] # for storing the bfs level by level
        level=[] # initial multiple roots to start traversal (rotten oranges)
        count=0 # to count all the rotten and fresh oranges
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]==2:
                    level.append([x,y])
                if grid[x][y]!=0:
                    count+=1
        queue.append(level)

        vector=[[-1,0],[1,0],[0,-1],[0,1]]
        minutes=0
        for level in queue:
            nodes=[] #for every new level
            while len(level)>0:
                prevx,prevy=level.pop(0)
                count-=1 # for every cell popped decrement count so we can see if we traversed all oranges
                for op in vector:
                    x=prevx+op[0]
                    y=prevy+op[1]
                    if x<0 or y<0 or x>len(grid)-1 or y>len(grid[0])-1 or grid[x][y]!=1:
                        continue
                    grid[x][y]=2 # converting fresh orange to rotten
                    nodes.append([x,y])
            if len(nodes)!=0:
                queue.append(nodes)
                minutes+=1

        if count>0:
            return -1
        # return len(queue)-1 # counting after the first level of rotten oranges therefore -1
        return minutes

# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
        

        