from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxArea = 0
        while l < r:
            if (r-l)*(min(height[l], height[r])) > maxArea:
                maxArea = (r-l)*(min(height[l], height[r]))
            if height[l] < height[r]:
                while l < r and height[l] > height[l+1]:
                    l += 1
                l += 1
            else:
                while l < r and height[r] > height[r-1]:
                    r -= 1
                r -= 1
        return maxArea

"""
4. Container with most water
This was easy, but I also seen it before
Took 10 minutes
Start with two pointers: one at the start and one at the end
Because its the mininum of the two columns that determine the area, the smaller column of the two cannot contribute
to a larger area by moving the other column inward
So we move the smaller column inward and try to find a bigger column along the way
This continues until the left and right pointer meet in the middle, then we end and we return our max area
"""