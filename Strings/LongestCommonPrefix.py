class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]
        for string in strs[1:]:
            common=""
            for i,j in zip(string,prefix):
                if i==j:
                    common+=i
                else:
                    break
            prefix=common
        return prefix
    
