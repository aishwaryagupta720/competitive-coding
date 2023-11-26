class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        frequency=1
        operations=0
        left,right=0,1
        nums.sort()
        state=nums[left]
        print(nums)
        while right<len(nums):
            if operations+((nums[right]-state)*(right-left))>k:
                while nums[right]==state:
                    frequence+=1
                    right+=1
            else:
                operations=operations+((nums[right]-state)*(right-left))
                state=nums[right]
                right+=1
                frequency+=1

        return frequency
