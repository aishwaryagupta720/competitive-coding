class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for index, value in enumerate(nums):
            y=target-value
            if y in dict:
                return [index,dict[y]]
            dict[value]=index
            

# Test Cases
# [2,7,11,15] 9
# [3,2,4] 6
# [3,3] 6
