# Lowerbound using left bisect - lowerbound works here because the start is unique
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        hashm=defaultdict(int)
        for i in range(len(intervals)):
            hashm[tuple(intervals[i])]=i
        
        intervals.sort()
        ans=[-1]*len(intervals)
        for start,end in intervals:
            index=bisect.bisect_left(intervals,[end,float("-inf")])
            if index<=len(intervals)-1:
                ans[hashm[(start,end)]]=hashm[tuple(intervals[index])]
        return ans
    
# Solution with Upperbound(counter-intuitive) and manual implementation 
    
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        for i in range(len(intervals)):
            intervals[i].append(i)
        intervals.sort()
        ans=[-1]*len(intervals)
        for index,i in enumerate(intervals):
            target=i[1]
            left=0
            right=len(intervals)
            while left<right:
                mid=(left+right)//2
                if intervals[mid][0]>target:
                    right=mid
                elif intervals[mid][0]<=target:
                    left=mid+1
            if intervals[left-1][0]==target :
                ans[i[2]]=intervals[left-1][2]
            elif left<len(intervals) and intervals[left][0]>=target:
                ans[i[2]]=intervals[left][2]
        return ans
        