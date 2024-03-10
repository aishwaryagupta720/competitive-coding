class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # utilise all elements in 1D array
        # unique elements in a row
        # minimum rows
        hashmap = Counter(nums)
        ans=[]
        while True:
            row=[]
            for key in hashmap:
                if hashmap[key]>0:
                    row.append(key)
                    hashmap[key]-=1
            if row:
                ans.append(row)
            else:
                break
        return ans

# You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

# The 2D array should contain only the elements of the array nums.
# Each row in the 2D array contains distinct integers.
# The number of rows in the 2D array should be minimal.
# Return the resulting array. If there are multiple answers, return any of them.

# Note that the 2D array can have a different number of elements on each row.

 

# Example 1:

# Input: nums = [1,3,4,1,2,3,1]
# Output: [[1,3,4,2],[1,3],[1]]