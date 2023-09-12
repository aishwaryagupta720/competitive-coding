class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_index = []

        for index,num in enumerate(nums):
            num_index.append([num,index]) 

        num_index.sort() #sorts on the first element inside lists in list [[*,x]]
        # print(num_index) #[[2, 1], [3, 0], [4, 2]] for [3,2,4]

        i=0
        j=len(num_index)-1
        while i<j:
            if num_index[i][0]+num_index[j][0]<target :
                i+=1
            elif num_index[i][0]+num_index[j][0]>target :
                j-=1
            else :
                return [num_index[i][1],num_index[j][1]]
   
