class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=left+1
        if len(s)==0:
            return 0
        counter=set(s[left])
        maxm=1
        current=1
        while(right<len(s)):
            if s[right] not in counter:
                if right<len(s)-1:
                    counter.add(s[right])
                    right+=1
                    current+=1
                else:
                    current+=1
                    break
            else:
                maxm=max(maxm,current)
                current=1
                right=left+2
                left=left+1
                counter=set(s[left])
        maxm=max(maxm,current)
        return maxm
                
# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
