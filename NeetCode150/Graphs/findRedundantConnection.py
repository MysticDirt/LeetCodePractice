from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #I remember use DFS to find topological sort and forward, backward, cross, and tree edges
        #A forward, backward, or cross edge would be what we're looking for.
        #So essentially, do a DFS until a node already visited is pointed to
        #Since we are given edges, we just put all seen nodes into a set until we get a repeat second edge
        #Only issue is we have to return the last edge

        #Watched neetcode video because I wanted to avoid making a whole graph just for DFS
        #So now Im using a disjoint set, using the union find algorithm (rank and parent)
        #This works because 1 <= ai < bi <= len(edges) is a constraint. Otherwise we would be forced to make a graph out of it 
        n = len(edges)
        rank = [1] * n
        parent = [i for i in range(1,n+1)]
        for a,b in edges:
            i = a-1
            j = b-1
            while i != parent[i-1]:
                i = parent[i-1]
            while j != parent[j-1]:
                j = parent[j-1]
            if i == j:
                return [a,b]
            elif rank[i-1] >= rank[j-1]:
                parent[j-1] = i
                rank[i-1] += rank[j-1]
            else:
                parent[i-1] = j
                rank[j-1] += rank[i-1]
        return[i,j]
    
"""
12. Redundant Connection
At first I tried seeing if I could do it through DFS and finding a non-tree edge, but it is probably impossible unless I build the graph first and then DFS
I decided there must be a way to do it without building a graph, so I watched the NeetCode solution
And the NeetCode solution was the disjoint set and the Union Find algorithm.
O(V+a(E)) Time complexity, a for amortized.
Since we have to find the original parent every edge, it is not simply O(V+E) like it would be for a graph.
But in this case, disjoint set is probably faster since it does not need the entire graph and I would not have to go back and find the last possible non-tree edge
This problem seems made to be solved with a disjoint set, even if its disguised as a graph problem
The rank and parent union find algorithm goes
- Rank means the size of the disjoint set that the element is a parent of
    - Initialize with all 1s (because every element starts off as its own set)
- Parent means the element above the current element
    - Initialize with 1 through n (every element is its own parent since it has no other parent)
So for each edge
- Find the furthest parent of each node (the while loops)
- If they both have the same parent (meaning they are already in a disjoint set), then the extra edge is introducing a cycle. Return that edge
- Otherwise, combine the sets
    - The parent with the higher rank stays the higher parent, the lower parent becomes a child
    - So set the lower rank parent's parent to the higher rank parent
    - Then add the rank of the lower rank's parent to the higher rank parent
- Repeat
I did a -1 for every index because Python is 0 indexed but the graph is 1 indexed.
In this problem, we're guaranteed a solution, so I just returned [i,j] for fun
"""