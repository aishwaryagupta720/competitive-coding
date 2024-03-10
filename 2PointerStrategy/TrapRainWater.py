class Solution:
    def trap(self, height: List[int]) -> int:
        water=0
        leftmax=0
        rightmax=0
        left=0
        right=len(height)-1
        while left<right:
            if height[left]<height[right]: 
                if height[left]>leftmax:
                    leftmax=height[left]
                else:
                    water+=leftmax-height[left]
                left+=1
            else:
                if height[right]>rightmax:
                    rightmax=height[right]
                else:
                    water+=rightmax-height[right]
                right-=1
        return water


# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.