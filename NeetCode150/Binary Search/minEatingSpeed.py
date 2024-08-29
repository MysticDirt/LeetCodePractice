from math import ceil
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(num):
            hours = 0
            for pile in piles:
                hours += ceil(pile / num)
            if hours <= h:
                #print("too big or equal", num)
                return False
                
            else:
                #print("too small", num)
                return True
                
        left = 1
        right = max(piles)
        while left < right:
            middle = (right // 2) + (left // 2)
            #print(middle)
            if (check(middle)):
                left = middle + 1
            else:
                right = middle
        return left
        
"""
3. Koko Eating Bananas
ACCEPTED SOLUTION:
I just looked at the solutions because I could not figure it out
- Turns out the solution is to literally guess and check with binary search
- We know the mininum has to be 1 and the maximum is the max pile
O(n log m) solution where m is the max number in piles and n is the length of piles
I did not think of guessing and checking. I tried to math it out this whole time.
Also, I seperated the right / 2 and left / 2 and then added it to avoid reaching integer max when adding it together
It worked for this problem but optimally it should be left + (right - left) / 2
"""


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        piles.sort()
        hours = [1]*n
        current = n - 1
        for i in range(h-n):
            hours[current] += 1
            anchor = ceil(piles[n-1] / (hours[n-1] + 1))
            #print(current, anchor, hours)
            if current > 0 and piles[current-1] > anchor:
                current -= 1
            else:
                current = n - 1
        #print(hours)
        maxpile = ceil(piles[n-1] / (hours[n-1]))
        for i in range(n-2, -1, -1):
            if hours[i] < hours[i+1]:
                maxpile = max(maxpile, ceil(piles[i] / (hours[i])))
            elif hours[i] == 1:
                break
        return maxpile

"""
THIS SOLUTION FAILS
O(n log n + h) time complexity
Fails to time with really large h
As of right now I distribute hours individually and calculate the max final bananas needed after distributing hours
But distributing hours will take a long while when there is integer max hours (like in a test case there) 
Spent 40 minutes so far, but I have to go back to the drawing board
"""
