class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def dfs(string,open,close):
            if open==close==n:
                ans.append(string)
                return
            if open<n:
                dfs(string+"(",open+1,close)
            if close<open:
                dfs(string+")",open,close+1)
        dfs("",0,0)
        return ans

#  Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]