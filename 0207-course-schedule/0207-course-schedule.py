from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        result: bool = False
        indegrees = [ 0 for _ in range(numCourses)]
        outgoing_edges = [ [] for _ in range(numCourses)]
        q = deque([])

        for prerequisite in prerequisites:
            course, condition = prerequisite
            indegrees[condition] += 1 
            outgoing_edges[course].append(condition)

            
        for index, indegree in enumerate(indegrees):
            if indegree == 0:
                q.append(index)

        for count in range(numCourses):
            if not q:
                return False
            
            node = q.popleft()
            
            for course in outgoing_edges[node]:
                indegrees[course] -= 1
                if indegrees[course] == 0:
                    q.append(course)

        return True

            
            




        


        
        