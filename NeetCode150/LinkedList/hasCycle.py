# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# --------------------------SOLUTION BELOW---------------------------------------
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = (fast.next).next
            if slow == fast:
                return True
        return False
"""
3. Linked List Cycle
- I solved this question before so it only took me 5 minutes
- But I did not know this way of solving it existed before then. I originally threw every pointer into a set and checked if I saw it again
- But this solution is O(n) time and O(1) space
- Algorithm
    - Have a fast and slow pointer
    - Make the fast pointer move two nodes at a time, while the slow pointer moves one node at a time
    - If the fast pointer and slow pointer end up pointing to the same node, there is a cycle
    - If the fast pointer reaches an end, then there is no cycle
- How it works:
    - A cycle is a loop in the linked list. 
    - The fast pointer will enter the cycle before the slow pointer
    - So intially, the fast pointer will be some distance ahead from the slow pointer by the time the slow pointer reaches the cycle.
    - And since the fast pointer is moving 2 at a time while the slow pointer is moving 1 at a time, the distance between them increases by 1 each move
    - So once the distance between the fast and the slow pointer reaches the length of the cycle, they will point to the same node, and we will know there is a cycle.
    - If there is no cycle, the pointers will never meet and the fast pointer will reach a null pointer eventually.
"""