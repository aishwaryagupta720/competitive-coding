class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj={i:[] for i in range(numCourses)}
        for course,pre in prerequisites:
            adj[course]+=[pre]
        
        white=set(adj.keys()) # all the courses to be visited
        grey = set() # all the course I am visiting (recursively)
        black= set() # all the course I have finished visiting

        def dfs(course):
            grey.add(course)

            for prereq in adj[course]:
                if prereq in grey:
                    return False
                if prereq in black:
                    continue
                if not dfs(prereq):
                    return False

            grey.remove(course)
            black.add(course)
            return True

        for course in white:
            ans = dfs(course)
            if not ans :
                return False
        
        return True
    
'''TOPOLOGICAL SORT - 
    1. Form Adjacency List 
    2. Run DFS on every element '''
    