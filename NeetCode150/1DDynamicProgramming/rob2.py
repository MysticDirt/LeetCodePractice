from typing import List
class Solution:
    def rob2(self, nums: List[int]) -> int:
        #My strategy is same as House Robber I but do it twice
        #One forward and one backward, and ignore the last one
        if len(nums) == 1:
            return nums[0]
        prevprev = nums[0]
        prev = max(nums[1],prevprev)
        current = prev
        for i in range(2, len(nums)-1):
            current = max(prevprev+nums[i],prev)
            prevprev = prev
            prev = current
        forward = current
        prevprev = nums[-1]
        prev = max(nums[-2],prevprev)
        current = prev
        for i in range(len(nums)-3,0,-1):
            #print(prev, prevprev, i)
            current = max(prevprev+nums[i],prev)
            prevprev = prev
            prev = current
            
        #print(current, forward)
        current = max(current, forward)
        return current

"""
4. House Robber II
O(n) time, O(1) space
Literally same thing as house robber 1, but I did it twice
I just did not consider the last one in the first run and I did not consider the first one in the second run
This time I only had 2 variables instead of 3 to make the code a little cleaner and be less redundant
"""