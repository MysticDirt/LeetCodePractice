from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle
        return -1
    
"""
1. Binary Search
Pretty simple binary search: iterative version
O(logn)
Since the array is sorted, if the number we are looking at is lower than our target, then  we need to look above for our target
If the number we are looking at is higher than our target, then we need to look below for our target
So we start at the middle, and if it is higher or lower then we reduce our range by looking only above or below that target
Then within that new range we find the middle and repeat
Here I treated left index as inclusive and right index as exclusive of the range, like how range() does it
"""