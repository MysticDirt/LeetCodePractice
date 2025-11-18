from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # This reminds me of a topological sort, where you can find dependencies using DFS.
        # It needs a discovery time in the thing.
        # prerequisites are directed edges
        # at the end of the day, we just need to find a cycle in the graph
        # so cant we just add a visited, do a dfs, and if we see it again its false?
        # First let's turn it into a dictionary of sets
        # would having prerequisites point to later classes or the classes point to prerequisiets be better?
        # it doesnt seem to matter
        courses = {}
        for edge in prerequisites:
            if edge[0] == edge[1]:
                return False
            if edge[0] in courses:
                courses[edge[0]].add(edge[1])
            else:
                courses[edge[0]] = {edge[1]}
        visited = set()
        for node in courses:
            if node in visited:
                continue
            stack = []
            stack.append(node)
            repeat_check = set()
            while stack:
                current = stack[-1]
                if current in repeat_check:
                    visited.add(current)
                    stack.pop()
                    continue
                if current in courses:
                    for child in courses[current]:
                        if child in repeat_check and child not in visited:
                            #print(current, child, visited, repeat_check)
                            return False
                        else:
                            stack.append(child)
                repeat_check.add(current)
        return True

"""
First attempt, way over the time. 
I will rewrite it with standard white, grey, black and maybe not the dictionary of sets but rather a list of lists.
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            courses[prerequisite[0]].append(prerequisite[1])
        visited = set()
        visiting = set()
        result = True
        def dfs(node):
            nonlocal result
            if node not in visited:
                if node in visiting:
                    result = False
                    return
                visiting.add(node)
                for neighbor in courses[node]:
                    dfs(neighbor)
                visiting.remove(node)
                visited.add(node)

        for i in range(numCourses):
            dfs(i)
        return result

"""
0 ms runtime, a lot better than 437ms
"""

        