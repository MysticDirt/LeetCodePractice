from typing import List


class Solution:
    
    def RPNHelper(self, tokens: List[str]) -> int:
        c = tokens[-1]
        tokens.pop()
        if c == "+" :
            return self.RPNHelper(tokens) + self.RPNHelper(tokens)
        elif c == "-":
            first = self.RPNHelper(tokens)
            second = self.RPNHelper(tokens)
            return second - first 
        elif c == "*":
            return self.RPNHelper(tokens) * self.RPNHelper(tokens)
        elif c == "/":
            first = self.RPNHelper(tokens)
            second = self.RPNHelper(tokens)
            return int(second / first) 
        else:
            return int(c)
    
    def evalRPN(self, tokens: List[str]) -> int:
        count = 0
        while tokens:
            count += self.RPNHelper(tokens)
        return count

"""
3. Evaluate Reverse Polish Notation
- Even though I did this before for homework, it still took me 25 minutes
- I tend to use recursion for most stack problems like this one, but performance does suffer in terms of time and space used
- Still O(n) time complexity though, but I have O(n) auxillary space (storing c for every call of RPNHelper)
Basically if it encounters an operator, it will do the operation using the next two down the stack
But if it encounters another operator, it will recursively handle it
It was bottom 15% in memory consistently though, but runtime it went 15% and then 98% so it does not matter
It is O(n) anyway
"""