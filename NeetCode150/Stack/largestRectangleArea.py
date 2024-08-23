from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #have a stack
        #push a pair of the height and the starting index
        #if the height is higher than the previous height, push pair of height and current index
        #if the height is lower than the previous height, 
            #first pop and calculate max areas off the stack
            #then push pair of height and earliest higher or same index
        #if height is the same as previous height, either skip or push previous index idk
        #at the end, pop the rest off the stack and calculate max area
        #max at the end is the max
        stack = []
        stack.append([heights[0], 0])
        max_area = 0
        for i in range(1, len(heights)):
            if heights[i] > heights[i-1]:
                stack.append([heights[i], i])
            elif heights[i] < heights[i-1]:
                earliest = -1
                while stack and stack[-1][0] > heights[i]:
                    earliest = stack[-1][1]
                    max_area = max(stack[-1][0] * (i - earliest), max_area)
                    stack.pop()
                stack.append([heights[i], earliest])
        while stack:
            max_area = max(stack[-1][0] * (len(heights) - stack[-1][1]), max_area)
            stack.pop()
        return max_area
    
"""
7. Largest Rectangle in a Histogram
CORRECT SOLUTION:
My first attempt is underneath this explanation
After coming back to this problem a day later I realized I had to rethink this problem
Adding columns to keep track of areas is impractical
Worst case every area remains viable, so I have to add to every area every iteration, making it O(n^2)
This problem seems to be solvable in O(n), so I went back to the drawing board
I needed to keep track of something I did not have to update every iteration
So I decided after much thinking to keep track of two things in a pair:
    - Column height
    - Rectangle width
Then multiplying those two would give an area that I can use to compare for maximum
But rectangle width I will have to update every time
So instead of rectangle width, I kept track of
    - Starting index
    Starting index is basically the index when that height becomes viable to make a rectangle
    So it would be the index after the last column shorter than our target column that is before our target column
        _______________
    ____|  
    ______________________
         ^ height of 2 becomes viable
But what to do if the columns goes 5, 4, 3: how do we know 3 was viable from the start?
The pattern is that since 5 is greater than 4 and 3, 4 and 3's starting index is the same as 5
So we use
    A stack
We keep a stack of a pair of column height and viable starting index
If the height increases from one column to the next, then that next column will have the current index as its starting index
    Because the one before it is lower, any column before it is not viable
If the height decreases from one column to the next, then for the previous column the following columns are not viable anymore.
So we can safely pop it off the stack and calculate its max area using the starting index and the position of our iterator
We keep popping it off the stack until we hit a column that is lower or equal to our current column
    Then that column's index + 1 is our new viable starting index.
Then at the end we pop everything off our stack, using the total length of the heights array instead of current index to
    calculate rectangle width and area
Then we return the max area
This solution is O(n)
Took me 2+ hours while being stuck on the old method, but after thinking of this it took me 10 minutes
But it took me 10 minutes to draw out this idea
My second ever LeetCode hard problem as I go through NeetCode 150
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #have a stack
        #push element onto stack
        #if element is lower than before, pop off stack to find width
        #keep track of max area along the way
        viable = []
        viable.append(0)
        n = len(heights)
        max_area = [0] * n
        max_area[0] = heights[0]
        single_max = 0
        for i in range(1, n):
            if heights[i-1] > heights[i]:
                j = len(viable) - 1
                while viable and heights[viable[j]] > heights[i]:
                    viable.pop(j)
                    j -= 1
            viable.append(i)
            for i in range(len(viable)):
                max_area[viable[i]] += heights[viable[i]]
            #print(max_area)
        single_max = max(max_area)
        #print(max_area)
        #now backward
        viable = []
        viable.append(n-1)
        for i in range(n-2, -1, -1):
            if heights[i+1] > heights[i]:
                j = len(viable) - 1
                while viable and heights[viable[j]] > heights[i]:
                    viable.pop(j)
                    j -= 1
            for k in range(len(viable)):
                max_area[viable[k]] += heights[viable[k]]
            viable.append(i)
            #print(max_area, i)
        #print(max_area)
        max_area.append(single_max)
        single_max = max(max_area)
        return single_max

"""
INCOMPLETE:
This answer is O(n^2) and fails the 1 spam testcase.
The thought process is:
    - If the next column is lower than the previous column, then that column is the height for any rectangle past it
    - If the next column is higher than the previous column, then both columns are still viable for any rectangle past it
I could not think of a way to rule out rectangles in a way where I only have to store 1 thing, so I made a max rectangle array
That array keeps track of the max rectangle possible with the column's height
So I have two loops, one that goes forward and one that goes backward.
The forward loop counts the rectangle that accounts for that specific rectangle and the ones past it
The backward loop counts the accounts for the rectangles on the ones before it
Then I add it together and get the highest possible rectangle.
HOWEVER, time complexity is O(n^2) because I have to update every viable rectangle on every iteration.
"""