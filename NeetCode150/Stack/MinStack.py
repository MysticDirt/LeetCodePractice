class MinStack:
    def __init__(self):
        self.stack = []
        self.ministack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.ministack:
            self.ministack.append(val)
        else:
            self.ministack.append(min(self.ministack[-1],val))

    def pop(self) -> None:
        self.stack.pop()
        self.ministack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.ministack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

"""
2. Min Stack
Took me 18 minutes, most of it was dealing with Python OOP
I only learned OOP in Java, C++, and C# so it took me a while to figure it out
I got 94% runtime and 70% memory so the solution seems good
I made two stacks, one that contains the values, and the other contains the minimum value at the time of the adding that value
So if I remove a value, all I have to do is remove it from the ministack and the new minimum would be the new top
It is probably possible to do it without another stack, maybe a dictionary containing indices and minimum values, to take up less space
"""