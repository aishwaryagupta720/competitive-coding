class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        def search(i,j,k):
            if k>=len(word):
                return True
            if i>=m or j>=n or i<0 or j<0 or word[k]!=board[i][j]:
                return False
            temp=board[i][j]
            board[i][j]=-1
            if search(i+1,j,k+1):
                return True
            if search(i,j+1,k+1):
                return True
            if search(i-1,j,k+1):
                return True
            if search(i,j-1,k+1):
                return True
            board[i][j]=temp
            return False

        for i,row in enumerate(board):
            for j,letter in enumerate(row):
                if letter==word[0]:
                    if search(i,j,0):
                        return True
        return False