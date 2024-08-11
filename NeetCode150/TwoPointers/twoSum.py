from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while(numbers[l] + numbers[r] != target):
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            #print(l, r)
        return [l + 1, r + 1]

"""
2. Two Sum II:
Used two pointers (like the category)
Took 10 minutes
Since its already sorted, start from the ends
If the number is too big, then decrease the right index to make it smaller
If the number is too small, then increase the left index to make it bigger
Since each test case is guaranteed a solution, that is all we need
"""