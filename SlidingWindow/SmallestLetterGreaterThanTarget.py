class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # find upperbound if no upperbound return letter[0]
        left=0
        right=len(letters)

        while left<right:
            mid=(left+right)//2
            if ord(letters[mid])<=ord(target):
                left=mid+1
            else:
                right=mid
        if left>len(letters)-1:
            return letters[0]
        else:
            return letters[left]

# You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

# Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

 

# Example 1:

# Input: letters = ["c","f","j"], target = "a"
# Output: "c"
# Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
# Example 2:

# Input: letters = ["c","f","j"], target = "c"
# Output: "f"
# Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.
# Example 3:

# Input: letters = ["x","x","y","y"], target = "z"
# Output: "x"
# Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].