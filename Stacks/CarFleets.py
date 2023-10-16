class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets=1
        pairs=[]
        for i in range(len(position)):
            pairs.append([position[i],(target-position[i])/speed[i]])
        pairs.sort()
        print(pairs)
        timetaken=pairs[-1][1]
        for i in range(len(pairs)-2,-1,-1):
            if pairs[i][1]<=timetaken:
                continue
            else:
                timetaken=pairs[i][1]
                fleets+=1
            # print(pairs[i])
        return fleets

# In my solution I have calculated time taken to reach destination. If the position of Car A is ahead of Car B , 
# but the time taken to reach for Car B is less than Car A, then they will catch up in the way and form a fleet, thats how I group them

# Example 1:
# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
# Output: 3
# Explanation:
# The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
# The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
# The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
# Note that no other cars meet these fleets before the destination, so the answer is 3.
