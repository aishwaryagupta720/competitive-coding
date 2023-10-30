class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            if target==nums[0]:
                return 0
            else: return -1
        # Finding the Rotation sand start of array(min element)
        low,high=0,len(nums)-1
        start=-1
        while low<high:
            mid=(low+high)//2
            if nums[mid]>nums[high]:
                low=mid+1
            else:
                high=mid
        start=low
        print(start)
        # dividing array into 2 parts , and searching in each
        low,high=0,start-1 
        if target>nums[high]:
                return -1
        while low<=high:
            if target<nums[low] or start==0:
                break
            mid=(low+high)//2
            if nums[mid]<target:
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
            else: return mid
        # part 2 of array
        low,high=start, len(nums)-1
        if target>nums[high]:
                return -1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]<target:
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
            else: return mid
        return -1




# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
#  or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Example 3:

# Input: nums = [1], target = 0
# Output: -1
