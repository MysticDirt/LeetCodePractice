from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #Dynamic programming, approach with assuming you know the optimal of smaller solutions
        #In this case, the optimal cost of the nth step is either
            #The cost of the n-1 step + optimal cost of reaching n-1
            #Or the cost of the n-2 step + optimal cost of reaching n-2
        #So we want to store the optimal cost of reaching n-1 and n-2
        #Then we compare if OPT(n-1) + COST(n-1) > OPT(n-2) + COST(n-2)
        #Optimal meaning minimal cost here
        optprevprev = cost[0]
        optprev = cost[1]
        if len(cost) <= 2:
            return min(cost[0],cost[1])
        total = 0
        for i in range(2,len(cost)):
            total = min(optprevprev, optprev) + cost[i]
            optprevprev = optprev
            optprev = total
        return min(optprev,optprevprev)
"""
2. Minimum Cost of Climbing Stairs
O(n) time, O(1) space
The way I approach optimum (min or max) dynamic programming problems is by thinking in optimal substructure
What subproblems can I break this into that I can use to build the solution?
In this case, the optimal solution for the nth step is:
    - min(optimal(n-2) + cost(n-2), optimal(n-1) + cost(n-1))
Since you can only go one or two steps, your choices are either going from the n-2 step or going from the n-1 step
Then you just choose the minimum.
So, we build up to the nth solution by creating the 1st, 2nd, 3rd, ..., n-2, n-1, and lastly nth solution
But in this case we only need to keep track of n-2 and n-1, keeping our space constant
So the solution is to just loop to the nth solution by finding the minimum of optimal(n-2) + cost(n-2) and optimal(n-1) + cost(n-1)
Then optimal(n-2) to optimal(n-1) and optimal(n-1) to optimal(n)
"""