class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numslist=nums
        nums=set(nums)
        counter=0
        for i in numslist:
            leftcounter=0
            rightcounter=0
            left=i
            right=i
            if i not in nums:
                continue
            while left-1 in nums:
                leftcounter+=1
                nums.remove(left-1)
                left-=1
            while right+1 in nums:
                rightcounter+=1
                nums.remove(right+1)
                right+=1
            if i in nums:
                nums.remove(i)
            counter=max(leftcounter+rightcounter+1,counter)
        return counter
            
                
            

