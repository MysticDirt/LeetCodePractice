from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        final = [1] * n
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        for i in range(n):
            final[i] = left[i] * right[i]
        return final

"""
7. Product of Array Except Self (No Division)
	- Did this before (what Headstarter asked for)
	- make 2 arrays, left and right, that takes the product of everything before it and after it
	- then multiply it together for final array
	- Took 10 minutes
	- Improvements:
	- The final loop and right loop can be merged into one loop, do right operation then final operation (but have to handle last element somehow)
	- initialize a list of default values is list l = [1] * n
	- But we didn't need the * n
"""