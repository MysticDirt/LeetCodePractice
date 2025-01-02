# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return None
        translate = dict()
        node = head
        new = Node(head.val, None, None)
        begin = new
        translate[node] = new
        node = node.next
        while node:
            new.next = Node(node.val, None, None)
            new = new.next
            translate[node] = new
            node = node.next
        node = head
        new = begin
        while node:
            new.random = translate.get(node.random, None)
            new = new.next
            node = node.next
        return begin

"""
6. Copy List with Random Pointer
Took me like 15 minutes
O(n) space, O(n) time
To deal with the random pointers, we need to be able to translate the original list nodes to new list nodes
So to do that in O(1) time you use a dictionary/hashmap
So the algorithm boils down to:
- First make the new nodes, and at the same time use the original node as a key to point to the new node in the translate dictionary
- Then run through the linked lists again, this time setting the random pointer using the original node's random and the translate dictionary
"""