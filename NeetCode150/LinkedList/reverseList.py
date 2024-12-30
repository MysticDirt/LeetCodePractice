# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
# --------------------------SOLUTION BELOW---------------------------------------
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        a = []
        node = head
        while node:
            a.append(node.val)
            node = node.next
        if a:
            result = ListNode(a[-1], None)
        else:
            return head
        new = result
        for i in range(len(a) - 2, -1, -1):
            new.next = ListNode(a[i], None)
            new = new.next
        return result

"""
1. Reverse Linked List
- Took me 5 minutes
- O(n) time
- O(n) space, (could be made O(1) space if I destroy the original list)
Algorithm:
- Iterate through the linked list and place all the values in an array
- Iterate through the array backwards and generate a linked list out of it
I used an array because I did not want to destroy the list. To save space complexity I would have just rerouted the pointers using temporary variables.
I also want to avoid recursion, so I used an array.
"""

        