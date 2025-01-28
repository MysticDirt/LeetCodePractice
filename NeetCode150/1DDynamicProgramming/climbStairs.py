class Solution:
    def climbStairs(self, n: int) -> int:
        #You can climb the stairs climbStairs(n-2) + climbStairs(n-1) ways since
        #you can either take 2 steps from 2 steps down or 1 step from 1 step down
        #to get to the next level.

        #This is the fibonnaci sequence. We'll save the last 2 numbers and keep adding
        prevprev = 0
        prev = 1
        total = 0
        for i in range(n):
            total = prev + prevprev
            prevprev = prev
            prev = total
        return total

"""
1. Climbing Stairs
I did this problem before in C++, so it only took me 5 minutes
To climb the nth step, you can do it in how many ways there are to climb n-2 steps + how many ways there are to climb n-1 steps
The reason is because to reach the nth step, you can either go 2 steps from n-2 or 1 step from n-1.
So the sequence is an = a(n-1) + a(n-2)
That is the Fibonacci sequence
So we store n-1 and n-2, and keep adding n times.
"""