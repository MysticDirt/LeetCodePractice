# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        a = []
        node = head
        while node:
            a.append(node)
            node = node.next
        if n == 1:
            if len(a) == 1:
                return None
            a[len(a)-2].next = None
        else:
            if n == len(a):
                return head.next
            a[len(a)-n-1].next = a[len(a)-n+1]
        return head

"""
5. Remove Nth Node From End of List
Above is my solution, though IT IS NOT OPTIMAL
Time Complexity: O(n), Space Complexity: O(n) (optimal space complexity is O(1))
Took me 15 minutes, mostly handling edge cases
Essentially, I put every node in a linked list, and then change the pointers for the node before to point to the node after the one being skipped.
However, I could instead use two pointers
- Have a fast pointer that skips n steps ahead
- Have a slow pointer that starts from the beginning
- Increment both by 1 until the fast pointer hits the end
- Then the slow pointer will be pointing at the Nth node from the end
- Then remove the node
Below is optimal
- The prev pointer is so that slow goes to n + 1 nodes from the end, because we need to change that node's next to the n - 1
- Time O(n), Space O(1)
"""
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prev = ListNode(-1, head)
        slow = prev
        fast = head
        for i in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return prev.next