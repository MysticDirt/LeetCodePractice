# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #Use BFS to clone graph
        if not node:
            return None
        new = Node(node.val, [])
        head = new
        queue = deque()
        nqueue = deque()
        visited = set()
        visited.add(node)
        queue.append(node)
        nqueue.append(new)
        nodestore = dict()
        nodestore[node.val] = new
        while queue:
            point = queue.popleft()
            new = nqueue.popleft()
            for thing in point.neighbors:
                #print(thing.val)
                if thing not in visited:
                    #print("visit", new.val)
                    queue.append(thing)
                    visited.add(thing)
                    newneb = Node(thing.val, [])
                    nodestore[thing.val] = newneb
                    nqueue.append(newneb)
                else:
                    newneb = nodestore[thing.val]
                new.neighbors.append(newneb)
                #print("new neb", new.neighbors)
        #print(head.val, head.neighbors)
        return head
"""
3. Clone Graph
O(V+E) time (checks all vertices, and checks the edges of each vertex)
O(V) space (nodestore, visited, queue, nqueue)
Did under 30 minutes.
This solution uses BFS to clone the graph. (It could be DFS too, just change popleft() to pop() on lines 26 and 27)
The main challenge after BFS is to make sure that the same value node in the graph is being pointed to by every other node in the graph that points to it.
That is why I have the nodestore, so I can store the addresses of the new nodes I made. In a dynamic programming style fashion, if it exists in nodestore, use it, if not, make a new one and add it to nodestore.
To further optimize in hindsight, I could have did away with the visited set and used nodestore to see if I visited the node already or not.
I used a queue both for the search and the creation (queue and nqueue respectively). 
    - queue was for the BFS
    - nqueue was to make the accurate copy of BFS
"""