class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        area=0
        while i<j:
            temp=min(height[i],height[j])*(j-i)
            # print(i,j,temp)
            area=max(area,temp)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return area

# input
# height = [1,8,6,2,5,4,8,3,7]
# Output 49
# Expected 49