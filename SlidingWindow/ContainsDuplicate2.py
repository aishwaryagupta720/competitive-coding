class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        left=0
        if k>len(nums)-1:
            right=len(nums)-1
        else:
            right=k
        if k==0:
            return False
        s=set(nums[left:right+1])
        while right<len(nums):
            s.add(nums[right])
            if len(s)==len(nums[left:right+1]):
                s.remove(nums[left])
                left+=1
                right+=1
            else:
                return True

        return False


# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false