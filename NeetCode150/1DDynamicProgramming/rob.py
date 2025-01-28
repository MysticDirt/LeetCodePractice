from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        #We can't rob adjacent houses
        #So if we rob the nth house, we cant rob the n-1 house
        #So if we rob the n-2 house, we cant rob the n-3 house and vice versa
        #Therefore, we have 3 choices when it comes to the nth house
            #n + OPT(n-2)
            #n + OPT(n-3)
            #0 + OPT(n-1)
        #The maximum of these is OPT(n)
        prevprevprev = nums[0]
        prevprev = 0
        prev = 0
        if len(nums) >= 2:
            prevprev = nums[1]
        else:
            return prevprevprev
        if len(nums) >= 3:
            prev = max(prevprev, nums[2] + prevprevprev)
        else:
            return max(prevprevprev, prevprev)
        current = prev
        for i in range(3, len(nums)):
            current = max(prevprevprev + nums[i], prevprev + nums[i], prev)
            prevprevprev = prevprev
            prevprev = prev
            prev = current
        return current
"""
3. House Robber
O(n) time, O(1) space
The nth house has this optimal value:
The maximum of
    - OPT(n-3) + value(n)
    - OPT(n-2) + value(n)
    - OPT(n-1)
OPT is optimal which is maximum value for the set of the kth house and below
When I looked at other solutions after solving it, they did not consider the first case.
Now I realize it is redundant because OPT(n-2) = OPT(n-3) if OPT(n-3) + value(n) is the maximum (since we consider OPT(n-1))
So you dont need the OPT(n-3), and you could only use 2 variables instead of 3, and make the code look a lot cleaner.
"""