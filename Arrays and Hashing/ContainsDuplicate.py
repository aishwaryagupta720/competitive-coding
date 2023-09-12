class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Brute Force O(n^2)
        # ans=False
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         print(nums[i],nums[j])
        #         if nums[i]==nums[j]:
        #             ans=True
        #             break
        #     if ans==True:
        #         break
        # return ans

        # O(nlogn)
        # nums=sorted(nums)
        # print(nums)
        # i=0
        # j=i+1
        # while i<j and j<len(nums):
        #     if nums[i]==nums[j]:
        #         return True
        #     else:
        #         i+=1
        #         j+=1
        # return False

        ## Time complexity-: o(n)
        ## memory complexity-: 0(n)

        return True if len(nums)!=len(set(nums)) else False







            

            
        