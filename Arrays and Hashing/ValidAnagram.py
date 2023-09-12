class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s=list(s)
        t=list(t)
        # replacement of sorted() , performs in place sorting , takes less memory
        # s.sort()
        # t.sort()
        # if s==t:
        #coverts to hashmap(dictionary)
        if Counter(s)==Counter(t):
        #sorts and returns a new list
        # if sorted(s)==sorted(t):  
            return True
        else:
            return False