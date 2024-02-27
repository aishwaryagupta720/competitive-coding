class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # define adjacency list
        adj = {i:[] for i in range(numCourses)}
        for course,pre in prerequisites:
            adj[course]+=[pre]

        # define recursive variables
        grey=set() #courses Im currently visiting recursively
        black=set() # courses Ive already visited
        ans=[] # answer list , as black SET changes order of input

        def dfs(course):
            grey.add(course)

            for prereq in adj[course]:
                if prereq in black:
                    continue
                if prereq in grey:
                    return False
                if not dfs(prereq):
                    return False

            grey.remove(course)
            if course not in black:
                ans.append(course)
                black.add(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return ans

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 