class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(x,y):
            if x<0 or y<0 or x>=len(board) or y>=len(board[0]):
                return
            if board[x][y]=="X" or board[x][y]=="T":
                return
            board[x][y]="T"
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)

        # find all O in the top and bottom border and all associated Os are marked T
        for x in [0,len(board)-1]:
            for y in range(len(board[0])):
                if board[x][y]=="O":
                    dfs(x,y)
        # find all O in the left and right border and all associated Os are marked T
        for y in [0,len(board[0])-1]:
            for x in range(len(board)):
                if board[x][y]=="O":
                    dfs(x,y)
        # all the remaining Os are marked X and the Ts are reverted to Os
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y]=="O":
                    board[x][y]="X"
                elif board[x][y]=="T":
                    board[x][y]="O"

# NOTE : If in a region O is on the border then the region is not converted to Xs , so we traverse and mark all the border touching areas first and convert the remaining Os to Xs

# 130. Surrounded Regions

# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.