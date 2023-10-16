class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer=[0 for i in range(len(temperatures))]
        stack=[(temperatures[0],0)]
        for i in range(1,len(temperatures)):
            days = 0
            j=len(stack)-1
            while j>=0:
                if stack[j][0]<temperatures[i]:
                    temp,index = stack.pop()
                    answer[index] = i-index
                    j-=1
                else:
                    break    
               
            stack.append((temperatures[i],i))
                
        return answer
    
# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]

# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
