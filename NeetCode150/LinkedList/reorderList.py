# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# --------------------------SOLUTION BELOW---------------------------------------
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node = head
        a = []
        while node:
            a.append(node)
            node = node.next
        node = head
        for i in range(1, len(a)//2 + 1):
            node.next = a[len(a)-i]
            node = node.next
            node.next = a[i]
            node = node.next
        node.next = None

        return head 
    
"""
4. Reorder List
MY SOLUTION ABOVE, NOT OPTIMAL
- O(n) time, O(n) space
Algorithm
- Put all nodes into an array of their order
- Put in the first node (basically do nothing since head stays head)
- Pull from the array all the remaining nodes and change their pointers in the way shown (n-1, 2, n-2, etc)
OPTIMAL SOLUTION
- O(n) time, O(1) space
Algorithm
- First find the middle node.
    - Have a fast pointer that goes through nodes 2 at a time
    - Have a slow pointer that goes through nodes 1 at a time
    - When the fast pointer reaches the end, the slow point is at the middle.
- Split off the middle node, so we have two linked lists
- Reverse the second list so it is in order of (n-1, n-2, n-3, ...)
- Then merge the two lists so that it alternates.
"""