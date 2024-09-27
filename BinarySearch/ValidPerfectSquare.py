class Solution:
    # search on answer set instead of index , as if I try to find multiples for a very large number , Time limit exceeds , so cannot search on multiples
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = (num//2)+1
        while left<=right:
            mid = left+(right-left)//2
            if num/mid>mid:
                left=mid+1
            elif num/mid<mid:
                right=mid-1
            else:
                return True
        return False

