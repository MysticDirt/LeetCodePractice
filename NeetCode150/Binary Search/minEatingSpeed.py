from math import ceil
from typing import List


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
