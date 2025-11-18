from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # So now its an actual topological sort. We'll have to mark the discovery time and the finish time, then sort by finish time. If we find a cycle (gray to gray) then return empty array.
        courses = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            courses[prerequisite[0]].append(prerequisite[1])
        visiting = set()
        visited = set()
        order = []
        bad = False
        def dfs(node):
            nonlocal bad
            if node not in visited:
                if node in visiting:
                    bad = True
                    return
                visiting.add(node)
                for neighbor in courses[node]:
                    dfs(neighbor)
                visiting.remove(node)
                visited.add(node)
                order.append(node)
        for i in range(numCourses):
            dfs(i)
        if bad:
            return []
        else:
            return order
            

        