# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# --------------------------SOLUTION BELOW---------------------------------------
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        result = ListNode(0, None)
        node = result
        while list1 or list2:
            if not list2 or (list1 and list1.val <= list2.val):
                node.next = ListNode(list1.val, None)
                list1 = list1.next
            else:
                node.next = ListNode(list2.val, None)
                list2 = list2.next
            node = node.next
        return result.next

"""
2. Merge Two Sorted Lists
- Took me about 10 minutes
- O(n) time
- Algorithm:
    - If list1 and list 2 exists, check between them and place the smaller value between them
    - If list1 exists and list2 does not, place list1
    - Vice versa for list2
    - Increment the nodes for the lists we use
    - Keep going until both lists are used up
"""