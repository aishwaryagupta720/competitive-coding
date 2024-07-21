class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=""
        for s in strs:
            length = len(s)
            ans=ans+str(length)+"*"+s
        return ans
    # 4*leet2*do
    def decode(self, s: str) -> List[str]:
        ans=[]
        i=0
        length=""
        while i<len(s):
            if s[i]!="*":
                length+=s[i]
                i+=1
            else:
                end=int(length)
                string=s[i+1:i+end+1]
                ans.append(string)
                i=i+end+1
                length=""
        return ans



