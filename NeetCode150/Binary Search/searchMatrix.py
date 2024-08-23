from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix)
        while bottom - top > 1:
            center = (top + bottom) // 2
            if matrix[center][0] == target:
                return True
            elif matrix[center][0] < target:
                top = center
            elif matrix[center][0] > target:
                bottom = center
        left = 0
        right = len(matrix[0])
        while left < right:
            middle = (left + right) // 2
            if matrix[top][middle] == target:
                return True
            elif matrix[top][middle] < target:
                left = middle + 1
            elif matrix[top][middle] > target:
                right = middle
        return False

"""
2. Search 2D Matrix
Took me about 15 minutes
I implemented 2 binary searches:
- A modified one that would find the biggest number smaller than the target on the first number of each column
    - The loop would stop when top and bottom are right next to each other rather than crossing each other
    - Then top would be the smaller number of the interval
- A regular one which would then search the row that the previous one landed on
This was O(log m + log n) = O(log(m*n)) which is what the problem asked for
"""