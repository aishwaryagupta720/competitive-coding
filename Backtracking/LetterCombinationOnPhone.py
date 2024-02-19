class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        alphabets=list("abcdefghijklmnopqrstuvwxyz")
        keypad={}
        answer=[]
        for i in range(2,10):
            if i==7 or i==9:
                count=4
            else:
                count=3
            keypad[i]=""
            while count>0:
                keypad[i]+=alphabets.pop(0)
                count-=1

        def dfs(sstr,count):
            if count==len(digits):
                if sstr=="":
                    return
                answer.append(sstr)
                return
            num=int(digits[count])
            for i in keypad.get(num):
                dfs(sstr+i,count+1)

        dfs("",0)  
        return answer  


# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
    
# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    
# Example 2:
# Input: digits = ""
# Output: []
    
# Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]