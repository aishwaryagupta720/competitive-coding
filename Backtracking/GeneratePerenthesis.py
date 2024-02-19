class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open=0
        closed=0
        answer=[]
        def dfs(sstr):
            nonlocal open,closed
            if open==n and closed==n:
                answer.append(sstr)
                return
            if open<n and closed<n:
                open+=1
                dfs(sstr+"(")
                open-=1
            if open>closed:
                closed+=1
                dfs(sstr+")")
                closed-=1
        dfs("")
        return answer


# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]