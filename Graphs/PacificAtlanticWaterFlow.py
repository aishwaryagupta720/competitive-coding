class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result=[]
        pacific,atlantic=set(),set()
        def dfs(x,y,path,prev):
            if (x<0 or y<0 
                or x>len(heights)-1 
                or y>len(heights[0])-1 
                or (x,y) in path 
                or heights[x][y]<prev):
                return
            path.add((x,y))
            dfs(x-1,y,path,heights[x][y])
            dfs(x+1,y,path,heights[x][y])
            dfs(x,y-1,path,heights[x][y])
            dfs(x,y+1,path,heights[x][y])

        for y in range(len(heights[0])):
            dfs(0,y,pacific,float("-inf"))
            dfs(len(heights)-1,y,atlantic,float("-inf"))
                
        for x in range(len(heights)):
            dfs(x,0,pacific,float("-inf"))
            dfs(x,len(heights[0])-1,atlantic,float("-inf"))

        for x in pacific:
            if x in atlantic:
                result.append(list(x))
        
        return result

"""
Here we have to find cells from where water can run off to both oceans , not the path of runoff but the 
topmost point from where it will go to both places . So we first find the cells from where water will runoff for each ocean 
Pacific - starting from each Top and Left row cells to the highest point 
Atlantic - starting from each Bottom and Right row cells to the highest point
these sets would contain all the cells from where water would runoff to the respective oceans , now we want the common cells ONLY so we find intersection
"""