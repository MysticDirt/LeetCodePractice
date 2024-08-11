from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        concave_area = 0
        l = 0
        r = len(height) - 1
        old = 0
        while l < r:
            concave_area += (r-l+1)*(min(height[l], height[r]) - old)
            old = min(height[l], height[r])
            #print(l, r, concave_area, old)
            if height[l] < height[r]:
                old_l = l
                while l < r and height[old_l] >= height[l+1]:
                    l += 1
                l += 1
            elif height[l] > height[r]:
                old_r = r
                while l < r and height[old_r] >= height[r-1]:
                    r -= 1
                r -= 1
            else:
                old_l = l
                old_r = r
                while l < r and height[old_l] >= height[l+1]:
                    l += 1
                l += 1
                while l < r and height[old_r] >= height[r-1]:
                    r -= 1
                r -= 1
        #print(l, r)
        if l == r:
            concave_area += height[l] - old
        area = sum(height)
        #print(concave_area)
        return concave_area - area
        
"""
5. Trapping Rain Water
- My first LeetCode Hard problem
- Took 35 minutes
O(n) time
The logic is simple, I calculated the convex area first and then subtracted the sum of the heights
I used a modified version of the maxArea contains most water algorithm
Only difference is that I increment both l and r if heights are equal, and instead of looking for max I add it
I also used old_l and old_r so that it compares with the previous maximum and not just the previous
    (That was my intention with the maxArea too, but it seemed like it did not matter for that problem)
I kept a concave area count and added the new "discovered" area which is just the distance between the new columns and
    the increased height
This problem was harder than the others except threeSum, but it did not feel that bad
However, I did get bottom 20% runtime consistently

MOST COMMON SOLUTION:
keep a left, right, max_left_height, and max_right_height
keep a water count
set left to 0, water to 0, right to end of list
set max_left_height to height at left and max_right_height to height at right
while the left is less than right
    if max_left_height is less than max_right_height
        increment left
        set max_left_height as the max of the max_left_height or the height of the new left
        increment water by max_left_height - height of new left
    else
        decrement right
        set max_right_height as the max of the max_right_height or the height of the new right
        increment water by max_right_height - height of new right
This solution is much simpler than mine. I did not think of using the other end to see if the other wall exists or not
And it iterates through the list once while mine iterates twice
"""