import sys
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #Bottom up dynamic programming looks like it
        #Watched neetcode video before attempting because im out of time
        #But it basically confirmed my hypothesis
        #Top down looks harder so, bottom up it is
        amount_to_coins = [sys.maxsize]*(amount+1) #dp array, but I like my arrays more descriptive
        amount_to_coins[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if i - coin >= 0:
                    amount_to_coins[i] = min(amount_to_coins[i - coin] + 1, amount_to_coins[i])
        #print(amount_to_coins)
        return amount_to_coins[-1] if sys.maxsize != amount_to_coins[-1] else -1

"""
8. Coin Change
First actual DP array problem I did on LeetCode
Watched NeetCode solution beforehand to confirm my strategy
O(amount * len(coins)) time, O(amount) space 
amount_to_coins holds the minimum number of coins needed to make that amount of money
The optimal relation is OPT = min(x + OPT(n-x)) for each x in coins
"""