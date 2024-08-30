from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0
        for right in range(1, len(prices)):
            profit = max(profit, prices[right] - prices[left])
            if prices[right] < prices[left]:   
                left = right
        return profit

"""
1. Best Time to Buy and Sell Stock
- O(n) time, iterates it through once
- Algorithm is just
    - Keep track of the minimum value we saw so far in the list
    - Compare prices to maximize profit against that minimum value for every value
"""