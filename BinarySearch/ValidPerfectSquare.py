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


# 367. Valid Perfect Square
# Solved
# Easy
# Topics
# Companies
# Given a positive integer num, return true if num is a perfect square or false otherwise.

# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

# You must not use any built-in library function, such as sqrt.

 

# Example 1:

# Input: num = 16
# Output: true
# Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
# Example 2:

# Input: num = 14
# Output: false
# Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
