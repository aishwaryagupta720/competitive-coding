class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        ans.add(())
        nums.sort()
        def dfs(i,subset):
            if i>=len(nums):
                return

            for k in range(i,len(nums)):
                ans.add(tuple(subset+[nums[k]]))
                dfs(k+1,subset+[nums[k]])
            return
        
        dfs(0,[])
        return list(ans)
    


# Given an integer array nums that may contain duplicates, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]