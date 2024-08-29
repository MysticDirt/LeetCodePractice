from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] < nums[right]:
                middle = (left + right) // 2
                if nums[middle] == target:
                    return middle
                elif nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle
            else:
                middle = (left + right) // 2
                if nums[middle] == target:
                    return middle
                elif nums[middle] >= nums[left]:
                    if target < nums[middle] and target >= nums[left]:
                        right = middle
                    else:
                        left = middle + 1
                else:
                    if target > nums[middle] and target <= nums[right]:
                        left = middle + 1
                    else:
                        right = middle
        return -1

"""
5. Search in Rotated Sorted Array
- Took 30 minutes
- O(log(n))
Same as finding minimum in sorted array but a few key differences:
- Once again we make sure the target is always between our left and right
- If our right is bigger than our left, then run a regular binary search
- Otherwise, we need to check more things
    - If the minimum is between the range
        - Choosing a middle will cause the minimum on one or the other side
        - If the minimum is on the left side, then the right side is continuous
            - So if the target is in between the middle and right, search that range
            - Else, search between left and middle
        - If the left side is continuous
            - If the target is in between the left and the middle, search that range
            - Else, search between middle and right
"""