class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindromes=[]
        def isPalindrome(string):
            if string==string[::-1]:
                return True
            else:
                return False

        def dfs(slice,substr):
            if len(slice)==1 :
                substr+=[slice]
                palindromes.append(substr)
                return
            if len(slice)==0:
                palindromes.append(substr)
                return
            for i in range(len(slice)):
                if isPalindrome(slice[:i+1]):
                    dfs(slice[i+1:],substr+[slice[:i+1]])

        
        dfs(s,[])
        return (palindromes)

# Given a string s, partition s such that every substring of the partition is a  palindrome . Return all possible palindrome partitioning of s.


# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:

# Input: s = "a"
# Output: [["a"]]