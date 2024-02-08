class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        found=False
        m=len(board)
        n=len(board[0])
        visited=set()
        def search(i,j,substring):
            nonlocal found,m,n
            if found==True or i>=m or j>=n or i<0 or j<0:
                return
            if (i,j) in visited:
                return
            if substring+board[i][j]==word:
                found=True
                return
            if substring+board[i][j] not in word:
                return
            visited.add((i,j))
            search(i+1,j,substring+board[i][j])
            search(i,j+1,substring+board[i][j])
            search(i-1,j,substring+board[i][j])
            search(i,j-1,substring+board[i][j])
            visited.remove((i,j))

        for i,row in enumerate(board):
            for j,letter in enumerate(row):
                if letter==word[0]:
                    search(i,j,"")
                    if found:
                        break
        return found