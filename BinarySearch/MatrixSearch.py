# log(m*n) time complexity
class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        # calculate the position of a number in matrix based on mid value
        #    apply generic binary search
        def calculate_position(index):
            col = index%cols
            row = index//cols
            return row,col
    
        left = 0
        right = (rows*cols)-1

        while left<=right:
            mid = left+(right-left)//2
            row,col = calculate_position(mid)

            if matrix[row][col]<target:
                left=mid+1
            elif matrix[row][col]>target:
                right=mid-1
            else:
                return True
        return False
    

# mlog(n) Time Complexity
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

