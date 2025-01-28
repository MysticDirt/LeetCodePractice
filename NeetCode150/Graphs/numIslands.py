from collections import deque
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #Matrix, think of graphs (adjacency matrix)
        #Nevermind, different strategy
        #Treat being neighbors as adjacencies for the graph, then run BFS
        #Ok to visit twice, just check visited set
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def bfs(row, col):
            q = deque()
            q.append((row,col))
            def check(i, j):
                if grid[i][j]=="1" and (i,j) not in visited:
                        q.append((i,j))
            directions = [[-1,0],[0,-1],[1,0],[0,1]]
            while q:
                i, j = q.popleft()
                for dr, dc in directions:
                    r, c = dr+i, dc+j
                    if r in range(rows) and c in range(cols):
                        check(r,c)
                visited.add((i,j))
                #print(position)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i,j)
                    islands += 1
                    #print("visit")
                #print(i,j)
        return islands
    
    """
    1. Number of Islands
    I watched the NeetCode video for this because I was trying to avoid rechecking the islands after the BFS/DFS, but turns out that is just the way to do it.
    The strategy here is to just run BFS to discover neighbors to build the island.
    Then add it to a visited set to prevent overcounting
    Issue is that this solution gets hit by time limit exceeded for large inputs even though it is O(m*n) still
    I assume it is because I am making a bunch of arrays and tuples for the visited set, and I am using Python which is normally slow
    It still passes the other test cases though.
    All accepted solutions destroy the island (turning all into 0 or 2 or anything but 1)
    That would avoid having a visited set and making all these arrays and tuples of size 2.
    
    ACCEPTED SOLUTION:
    Funnily enough, just changing popleft() to pop() made it faster. That does change it from BFS to DFS though
    complete code below
    Also, I discovered another reason why it was slow, but I discovered it in the Max Area of Island problem. So read the bottom comments on that one.
    """

from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #Matrix, think of graphs (adjacency matrix)
        #Nevermind, different strategy
        #Treat being neighbors as adjacencies for the graph, then run BFS
        #Ok to visit twice, just check visited set
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(row, col):
            q = deque()
            q.append((row,col))
            directions = [[-1,0],[0,-1],[1,0],[0,1]]
            while q:
                i, j = q.pop()
                for dr, dc in directions:
                    r, c = dr+i, dc+j
                    if r in range(rows) and c in range(cols):
                        if grid[r][c]=="1" and (r,c) not in visited:
                            q.append((r,c))
                visited.add((i,j))
                #print(position)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    islands += 1
                    #print("visit")
                #print(i,j)
        return islands

    

    