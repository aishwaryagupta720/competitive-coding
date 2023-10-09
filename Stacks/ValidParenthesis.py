class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in "{[(":
                stack.append(i)
            elif i in ')':
                if len(stack)==0 or stack[-1]!="(":
                    return False
                else:
                    stack.pop()
            elif i == '}':
                if len(stack)==0 or stack[-1]!="{":
                    return False
                else:
                    stack.pop()
            else: 
                if len(stack)==0 or stack[-1]!="[":
                    return False
                else:
                    stack.pop()
        if len(stack)==0:
            return True
        else:
            return False
        
# Input
# s ="(]"
# Output
# false
# Expected
# false