from collections import deque
from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #Treat being neighbors as adjacencies for the graph, then run DFS
        #Ok to visit twice, just check visited set
        #Just during DFS, count how many 1s we find
        #Then keep track of the max
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        maximum = 0

        def dfs(row, col):
            q = deque()
            q.append((row,col))
            directions = [[-1,0],[0,-1],[1,0],[0,1]]
            size = 0
            visited.add((row,col))
            while q:
                i, j = q.pop()
                for dr, dc in directions:
                    r, c = dr+i, dc+j
                    if r in range(rows) and c in range(cols):
                        if grid[r][c]==1 and (r,c) not in visited:
                            q.append((r,c))
                            visited.add((r,c))
                size += 1
                #print(size, q)
            return size
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    maximum = max(maximum, dfs(i,j))
                    #print("visit")
                #print(i,j)
        return maximum
    
"""
2. Max Area of Island
I just copy and pasted the code from Number of Islands and instead of counting the amount of islands, I counted the maximum.
In the DFS method I added a size counter and returned the value. Then I checked if it was the maximum we saw so far in the loop.
Did under 30 minutes.
One thing is that the Number of Islands code added islands to the visited set AFTER processing them.
    - This was bad because then nothing is stopping islands from being added to the stack twice.
    - This was not caught in the Number of Islands problem because it was all still part of the same island.
    - However, this could have contributed to the Time Limit Exceeded problem that I was having if I was checking many duplicate cells in the grid.
So remember, add nodes to the visited set WHEN SEARCHING AROUND (adding to the stack or queue) and not once processed (removing from the stack or queue).
"""