class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # upperbound and lowerbound
        if not nums or target not in set(nums):
            return [-1,-1]
        left=0
        right=len(nums)
        # upperbound
        while left<right:
            mid=(left+right)//2

            if nums[mid]<=target:
                left=mid+1
            else:
                right=mid

        upperbound=left-1

        # lowerbound
        left,right=0,len(nums)
        while left<right:
            mid=(left+right)//2

            if nums[mid]>=target:
                right=mid
            else:
                left=mid+1
        
        lowerbound=left
        return [lowerbound,upperbound]




        