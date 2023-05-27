class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares=[0]*len(nums)
        index=len(nums)-1
        left,right=0,len(nums)-1
        while left<=right:
            numleft= nums[left]**2
            numright= nums[right]**2
            if left<right:
                if numleft<numright:
                    squares[index]=numright
                    right-=1
                elif numleft>numright:
                    squares[index]=numleft
                    left+=1
                else :
                    squares[index],squares[index-1]=numleft,numright
                    left+=1
                    right-=1
                    index-=1
                index-=1
            else:
                squares[index]=numleft
                break
        return squares



# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]