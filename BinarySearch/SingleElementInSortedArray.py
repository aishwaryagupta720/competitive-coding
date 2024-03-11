class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        if left==right:
            return nums[left]
        if nums[left]!=nums[left+1]:
            return nums[left]
        if nums[right]!=nums[right-1]:
            return nums[right]
        while(left<=right):
            mid=(left+right)//2
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            elif nums[mid]==nums[mid-1] and mid%2!=0 or nums[mid]==nums[mid+1] and mid%2==0:
                left=mid+1
            else:
                right=mid-1
        
        
# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

 

# Example 1:

# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:

# Input: nums = [3,3,7,7,10,11,11]
# Output: 10