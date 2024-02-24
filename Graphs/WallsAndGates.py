class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        queue=collections.deque([])
        for x in range(len(rooms)):
            for y in range(len(rooms[0])):
                if rooms[x][y]==0:
                    queue.append([x,y])
        
        vector=[[0,1],[0,-1],[1,0],[-1,0]]
        while len(queue)>0:
            prevx,prevy=queue.popleft()
            for op in vector:
                x=prevx+op[0]
                y=prevy+op[1]
                if x<0 or y<0 or x>len(rooms)-1 or y>len(rooms[0])-1 or rooms[prevx][prevy]+1>rooms[x][y]:
                    continue
                rooms[x][y]=rooms[prevx][prevy]+1
                queue.append([x,y])