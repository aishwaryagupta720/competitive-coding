class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(s1 for s1 in s if s1.isalnum())
        s=s.lower()
        print(s)
        i=0
        j=len(s)-1
        while i<=j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True



