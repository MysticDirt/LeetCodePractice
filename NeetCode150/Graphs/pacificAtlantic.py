from typing import List
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #INITIAL THOUGHTS
        #Use DFS here, get to ocean faster
        #Trapped cells (ones that cannot move anymore), we can just set status of trapped,
            #can reach pacific, can reach atlantic, can reach both (maybe call it -1, -2, -3, -4)
        #Start on the outside, then we move inward (more likely outside ends earlier)

        #Actually, we lose height information if we do that so
        #We dfs from middle, and then the path taken is assumed to be able to go pacific/atlantic. Then we do not have to search for routes for that side.
        #So store if pacific/atlantic/both/neither in a seperate 2D array
        #Or outside in works when we check heights too

        #-----REAL------

        # Just watched neetcode video. Outside in is the correct approach, but we 
        # start the dfs at the border and climb UP to find where pacific and atlantic can reach
        # Here either dfs or bfs works actually
        rows = len(heights)
        cols = len(heights[0])
        pvisited = set()
        avisited = set()
        
        def dfs(row,col,visited):
            if (row,col) in visited:
                return
            directions = [[1, 0],[0,1],[-1,0],[0,-1]]
            stack = []
            stack.append((row,col))
            visited.add((row,col))
            while stack:
                row,col = stack.pop()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r in range(rows) and c in range(cols) and (r,c) not in visited:
                        if heights[r][c] >= heights[row][col]:
                            stack.append((r,c))
                            visited.add((r,c))

        for i in range(rows):
            dfs(i,0,pvisited)
            dfs(i,cols-1,avisited)

        for j in range(cols):
            dfs(0,j,pvisited)
            dfs(rows-1,j,avisited)

        result = []
        for r,c in pvisited:
            if (r,c) in avisited:
                result.append([r,c])
        return result
        
"""
6. Pacific Atlantic Water Flow
O(m*n) time complexity
O(m*n) space complexity
I watched the neetcode video because I hit the 30 minute mark without a completely clear idea
The idea to avoid repeat work is to instead of running a DFS going downhill on each cell, run a DFS going uphill from the border.
Every cell where both the Pacific DFS and the Atlantic DFS reach is the result
Here BFS would also work, as it is just the fact that it is a graph traversal that matters
"""

