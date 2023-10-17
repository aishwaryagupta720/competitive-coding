class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i=len(matrix)
        for array in matrix:
            left=0
            right=len(array)-1
            if array[right]<target:
                continue
            if array[left]>target:
                return False
            while left<=right:
                mid=(left+right)//2
                if array[mid]>target:
                    right=mid-1
                elif array[mid]<target:
                    left=mid+1
                else :
                    return True
            i-=1
            if i<1:
                return False
            
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

