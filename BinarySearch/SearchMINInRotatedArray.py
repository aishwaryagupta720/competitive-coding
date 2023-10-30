class Solution:
    def findMin(self, nums: List[int]) -> int:
        low,high=0,len(nums)-1
        mid = (low+high)//2
        if nums[mid]>=nums[low] and nums[mid]<=nums[high]:
            return nums[0]
        while low<=high:
            mid = (low+high)//2
            if nums[mid]>=nums[low] and nums[mid]>nums[high]:
                low=mid+1
            else :
                if nums[mid-1] and nums[mid-1]>nums[mid]:
                    return nums[mid]
                high=mid-1
            print(low,high)
        return nums[mid]


# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

# Example 3:

# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

