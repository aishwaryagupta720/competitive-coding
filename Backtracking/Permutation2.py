class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        prev=-11
        def dfs(perm,array):
            nonlocal prev
            if len(array)==0:
                ans.add(tuple(perm))
                return
            for i in range(len(array)):
                if len(perm)==0 :
                    if prev==array[i]:
                        continue
                    prev=array[i]
                temp=array[:]
                temp.pop(i)
                dfs(perm+[array[i]],temp)
        dfs([],nums)
        return list(ans)
    
# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

# Example 1:

# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# Example 2:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# # 