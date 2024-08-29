from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] < nums[right]:
                return nums[left]
            else:
                middle = (left + right) // 2
                if nums[middle] >= nums[left]:
                    left = middle + 1
                else:
                    right = middle
        return nums[left]

"""
4. Minimum of Rotated Sorted Array
Took me like 15 minutes
O(logn) time
Logic is
- Keep the minimum within range at all times
- If the left number is less than the right number
    - Then it must be the minimum
- Otherwise
    - The minimum is somewhere between (or the right I guess)
    - So we find the middle
        - If that middle is less than the left
            - Then the minimum must be between the left and middle
            - So set the new right to the middle
        - Otherwise
            - Then the minimum must be between the middle and right
            - So set the new left to the middle + 1
I could have put the nums[left] < nums[right] condition in the while loop

Most common solution:
- Same thing but they dont have the left less than right condition
- Instead they just loop if right >= left + 1
"""
