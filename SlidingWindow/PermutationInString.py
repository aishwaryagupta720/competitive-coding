class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars=Counter(s1)
        left,right=0,len(s1)-1
        counter=Counter(s2[left:right+1])
        while right <len(s2):
            print(counter)
            if chars==counter:
                return True
            else:
                if counter[s2[left]]==1:
                    del counter[s2[left]]
                else:
                    counter[s2[left]]-=1
                left+=1
                right=left+len(s1)-1
                if right<len(s2):
                    counter[s2[right]]+=1
        return False
            

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false