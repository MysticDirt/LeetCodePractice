from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        result = [0] * n
        for i in range(n-1):
            while stack:
                if stack[-1][0] < temperatures[i]:
                    result[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()
                else:
                    break
            if(temperatures[i] < temperatures[i+1]):
                result[i] = 1
            else:
                stack.append((temperatures[i], i))
        while stack:
            if stack[-1][0] < temperatures[n-1]:
                result[stack[-1][1]] = n-1 - stack[-1][1]
                stack.pop()
            else:
                break
        return result
    
"""
5. Daily Temperatures
Took me about 20 minutes
At first I thought of reverse traversing the array and keeping a min stack, but upon further thinking that was not plausible
There is the possibility that two colder days can be between two hotter days, but one colder day is hotter than the other
So I came up with this solution instead:
- When we traverse the array:
    - If the next element is higher than the current element, then the number of days we have to wait is one
    - Otherwise, it depends on the elements after it
- After we find a day that is warmer than a previous day, we do not have to care about the previous day anymore
    - So when we store the days that do not have a warmer day found yet, the day after will always be colder than the previous day
    - And the later and colder day will always find a warmer day before or on the same time as the warmer day
    - So a stack will be sufficient
        - When a day does not have an immediate warmer day, push it on the stack
        - When a warmer day is found, pop it off the stack and compare the next
    - The last day is always 0. We have to check it to compare the stack, but we will not push it to the stack.
    - I pushed a tuple of the temperature and the index.
        - In hindsight I did not need to do that, I just needed the index. I can access the temperature through the index.
        - Then I save memory.
This solution is O(n). Even though multiple stack iterations may happen in a single array iteration, 
    the total iterations for the stack is n or less, and the total iterations for the array is n.

The most common solution is similar to mine but there was no need for the case of checking the +1. The stack would handle that
case already. Then the final step also would not have to be outside of the loop, because putting the last index in there does not
do anything, whereas trying to access an array out of bounds would do something.
"""