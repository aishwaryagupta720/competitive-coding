class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictnry={} # implementation similar to Counter
        for i in nums:
            dictnry[i]=dictnry.get(i,0)+1
        # empty list of list
        asos=[[] for i in range(len(nums)+1)]# cannot do asos=[[]]*len(nums)+1 as append to list of list does not work
        # moving the numbers at the [no of times repeated] index in list , multiple elements with same times repeatition will be in list of list 
        for nums,count in dictnry.items():
            print(nums,count)
            asos[count].append(nums)
        print(asos)
        temp=[]
        # returning k most frequent elements
        for i in range(len(asos)-1,-1,-1):
            if k==0:
                break
            if asos[i]==[]:
                continue
            else: 
                for l in asos[i]:
                    temp.append(l)
                    k-=1
        return temp