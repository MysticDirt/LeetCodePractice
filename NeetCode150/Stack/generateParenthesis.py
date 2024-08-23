from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def help(left, right, s):
            if len(s) == n * 2:
                result.append(s)
                return 

            if left < n:
                help(left + 1, right, s + '(')

            if right < left:
                help(left, right + 1, s + ')')

        result = []
        help(0, 0, '')
        return result

"""
4. Generate Parenthesis
This one took me 4+ hours, and I eventually gave up and saw the solutions
At first I tried it in like a dynamic programming style, using the previous generated strings to make new ones
The theory was that the n possible strings would be:
    - "()[n-1]"
    - "([n-1])"
    - "[n-1]()"
However, that ended up not being true. Invalid strings of n-1 could create a valid n string in the second option
Like "())(()" is not valid but "(())(())" is valid, and my approach missed those
So after a lot of time with that I tried a different approach, which would be to figure out where the ( has to be
to generate all valid strings and then put ) for the other indices
However, I got stuck on trying to loop it:
Lets say we have to make an n=5 string.
- Lets call each open parenthesis a, b, c, d, and e depending on how far right it is
- The first open parenthesis has to be at the start to be valid, so lets call this index a = 0
- Then b has two options, either a + 1 = 1 or a + 2 = 2, because there can only be at most 1 closing parenthesis between a and b
- Then c has a range between b + 1 and index 4 inclusive. There can at most be 2 closing parenthesis behind it to match a and b,
    so the farthest right it can go is the 5th position
- Then d has a range between c + 1 and 6, then e has a range between d + 1 and 8. 
If, we add f, g, h, etc.. it would go in the same pattern.
But to generate these all I would have to do n! loops based on a variable n.
I would have to loop e inside of d inside of c inside of b
The way to do that is recursion + loops but I did not figure it out.

CURRENT SOLUTION:
It uses recursion
In the function, we recursively build different strings
If the left has less open parenthesis than what we need, add one
If the right has less closed parenthesis than open parenthesis, add a closed parenthesis
We do both checks and both recursions in each call, so it eventually build all the strings needed
Then we return the final result
"""