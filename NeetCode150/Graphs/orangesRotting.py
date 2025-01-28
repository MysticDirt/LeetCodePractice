from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #Similar to maximum shortest path in a graph
        #Use BFS
        #If we find a 1, search for an adjacent 2, then BFS off of the 2. If no adjacent 2, return -1
        #This time, we'll just change the grid rather than using visited sets
        #We'll mark with 2s what was rotten, and once the group is done just delete it (turn into 0)

        #Didnt work, change of strategy:
            #If there are multiple 2s in the same group, it would instead just simulate the time from one rotten orange instead of all of them
            #We need it for all of them
        #Find all 2s and put it in the queue
        #keep track of when each orange rotted using the grid during BFS (in this case it was 2*time in the grid)
        #count the 1s for each fresh one
        #if theres some fresh oranges left over after the BFS, then return -1 since it never got reached

        rows = len(grid)
        cols = len(grid[0])
        minutes = 0
        queue = deque()
        fresh = 0

        def rotBFS(queue):
            nonlocal fresh
            directions = [[-1,0],[0,-1],[0,1],[1,0]]
            time = 0
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r in range(rows) and c in range(cols):
                        if grid[r][c] == 1:
                            grid[r][c] = 2 + grid[row][col]
                            time = max(time, grid[row][col])
                            queue.append((r,c))
                            fresh -= 1
                grid[row][col] = 0
            time = int(time/2)
            return time
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row,col))
                elif grid[row][col] == 1:
                    fresh += 1

        minutes = rotBFS(queue)
        if fresh == 0:
            return minutes
        else:
            return -1

"""
5. Oranges Rotting
- O(m * n) time complexity
- Have to use BFS in this case (since its basically longest shortest path, classic BFS problem)
- And that we are doing it simutaneously with all rotten oranges at the same time, it has to be BFS so the closest rotten orange is used
As seen from my top comments, my original strategy did not work since I did one rotten orange at a time and then deleted all the ones it rotted
So if multiple rotten oranges are in the same orange cluster, my algorithm failed
So I changed it so that I search for all the rotten oranges and add it to the BFS queue, and then run BFS.
The fresh counter is so that if fresh oranges remain after rotting, we return -1.
Originally I searched the array again for fresh oranges remaining, but the fresh counter makes it so I only have to search once
    - This case is still O(m * n) time complexity though anyway, just iterating fully twice (for a total of three with the BFS)
"""        