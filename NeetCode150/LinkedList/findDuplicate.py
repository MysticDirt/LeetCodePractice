from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd's algorithm: treat as linked list, then find beginning of cycle
        fast = 0 
        slow = 0
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        final = 0
        while slow != final:
            slow = nums[slow]
            final = nums[final]
        return final

"""
8. Find the Duplicate Number
O(n) time, O(1) space
I had to watch the NeetCode video for the logic of this problem.
When I first looked at this problem I was wondering why it was in the linked list category
However, it is easier to see the optimal solution when considering it as a linked list with a cycle
The constraints of this array are that it is length n + 1, has elements 1 <= x <= n, and only has one duplicate number
However the duplicate number can appear as many times as it wants.
At first I thought of the bitwise XOR solution, but that fails here because the duplicate number can appear as many times as it wants.
But to understand why this solution works, lets see this problem as a linked list problem
We are given an array with those conditions, lets say [1, 3, 4, 2 ,2]
Then, if we consider indices, it would look like:
i:  0 1 2 3 4
n: [1 3 4 2 2]
Since the array values can only be between 1 and n, each index is essentially pointing to another index. It is just that one index is pointed to multiple times.
So mapping it out on a linked list:
i:  0 1 2 3 4
n: [1 3 4 2 2]
0 -> 1 -> 3 -> 2 -> 4
               ^----|
The duplicate element causes a cycle.
Each index only appears once EXCEPT FOR ONE. So there will only be one cycle.
Now all we have to do is find the element where the cycle begins. 
For a linked list, this algorithm is called Floyd's algorithm, which is O(n).
You have a fast pointer and a slow pointer. Fast one moves two at a time, slow moves one at a time.
In the Has Cycle problem I explained how this algorithm finds out whether a cycle exists. 
Eventually, with a cycle, the fast and slow pointer will meet again.
Let's say the cycle is p nodes away from the start of the linked list.
Then the slow pointer will travel p nodes to get to the start of the cycle.
Then the fast pointer will travel 2p nodes, meaning it will be p nodes into the cycle.
For each iteration, the distance between the fast pointer and the slow pointer increases by 1 (slow moves 1, fast moves 2, 2 - 1 = 1)
For the fast and slow pointer to meet, the distance between the fast and slow pointer has to be some multiple of the number of nodes in the cycle.
Lets call the number of nodes in the cycle c. Then the fast pointer has to make a gap of n*c nodes for some positive integer n.
N depends on how big p is compared to c. n = p//c + 1 (Where // is int division)
But to reach that multiple of c, the fast and slow pointer only have to move n*c - p times, since they already moved p times and just need to reach the next multiple of c.
Here: 0 =< n*c - p < c. It is just the amount left in the cycle before the two pointers meet.
So the fast and slow pointer meet n*c - p nodes after the beginning of the cycle. 
But if the beginning of the cycle is at 0, c, up to n*c, then n*c - (n*c - p) = p. We are p nodes away from the beginning of the cycle.
So lastly, we just create another slow pointer at the start of the linked list, and keep moving both slow pointers until they match.
Then both slow pointers moved p times, and they reached the beginning of the cycle, which in this case is the duplicate element of the array.
So the algorithm is
- Initialize fast and slow pointers
- Move slow pointer once and fast pointer twice
    - Here, moving means setting the number to the value at that index of nums (that is us traversing through the linked list)
- While slow and fast pointers are not equal
    - Keep moving the slow pointer by one and fast pointer by two
- At this point the fast and slow pointers are equal, so
- Create a new pointer at the start (I called it final)
- While slow and final are not equal
    - Keep moving both pointers one at a time
- Then return final (or slow). That is the duplicate element/beginning of the cycle.
"""