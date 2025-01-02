# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0, None)
        node = head
        while l1 or l2:
            if l1:
                node.val += l1.val
                l1 = l1.next
            if l2:
                node.val += l2.val
                l2 = l2.next
            if node.val > 9:
                node.next = ListNode(node.val // 10, None)
                node.val = node.val % 10
            else:
                if l1 or l2:
                    node.next = ListNode(0, None)
            node = node.next
        return head

"""
7. Add Two Numbers
Time Complexity: O(n)
Space Complexity: O(1)
Took me like 15 minutes
Algorithm:
- Make a new node
- Set its value to the sum of the two corresponding nodes
- If over 9 (even if it is 9 or under, doing this will not change anything)
    - Get the carry value by integer dividing by 10 and add it to the next node
    - Mod the original value by 10 to get just the digit
- If there are still digits left in the original lists, make a new node
- Move the pointers down the lists
- Then repeat
"""